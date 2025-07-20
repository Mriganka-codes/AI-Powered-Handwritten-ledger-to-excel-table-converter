import os
import json
import io  # Required for in-memory file handling
import pandas as pd
import google.generativeai as genai
from flask import Flask, request, send_file, jsonify
from dotenv import load_dotenv
from PIL import Image
import re

load_dotenv()

# --- Configuration for Validation ---
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MAX_FILE_SIZE_MB = 5
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

app = Flask(__name__, static_folder='.', static_url_path='')

# --- Helper function for file validation ---
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_gemini_response(image, prompt):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([image, prompt])
    return response.text

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/about')
def about():
    return send_file('about.html')

@app.route('/how-it-works')
def how_it_works():
    return send_file('how-it-works.html')

@app.route('/api/convert', methods=['POST'])
def convert_image_to_excel():
    # --- 1. Robust Input Validation ---
    if 'image' not in request.files:
        return jsonify({"error": "No image part in the request"}), 400
    
    image_file = request.files['image']

    if image_file.filename == '':
        return jsonify({"error": "No image selected for uploading"}), 400

    if not allowed_file(image_file.filename):
        return jsonify({"error": f"Invalid file type. Please use {', '.join(ALLOWED_EXTENSIONS)}."}), 400
        
    # Check file size by checking the content length of the request
    if request.content_length > MAX_FILE_SIZE_BYTES:
        return jsonify({"error": f"File is too large. Maximum size is {MAX_FILE_SIZE_MB} MB."}), 413

    # --- 2. Secure and Error-Proof Image Loading ---
    try:
        image = Image.open(image_file.stream)
    except IOError:
        return jsonify({"error": "Could not read image file. It may be corrupted."}), 400

    prompt = """
    Analyze the following image. It contains a data table.
    Extract all the information from the table. Your output must be a valid JSON object.
    The JSON object should contain a single key called "records". The value should be an array of objects, where each object represents a row from the table.
    Use the table's column headers as the keys for each object.
    Ensure that any values that are numbers are formatted as numbers, not strings.

    Do not include any text or explanations outside of the JSON output.
    """

    try:
        response_text = get_gemini_response(image, prompt)
        
        json_match = re.search(r'```json\s*(\{.*?\})\s*```', response_text, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
        else:
            json_str = response_text.strip()

        data = json.loads(json_str)
        df = pd.DataFrame(data['records'])

        # --- 3. Efficient In-Memory File Handling ---
        # Create a virtual file in memory
        output_io = io.BytesIO()
        df.to_excel(output_io, index=False, engine='openpyxl')
        output_io.seek(0) # Go to the beginning of the memory buffer

        return send_file(
            output_io,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name='output.xlsx'
        )

    except json.JSONDecodeError:
        error_message = f"Failed to decode JSON. AI Response was: {response_text}"
        print(error_message)
        return jsonify({"error": "The AI returned an invalid data format. Please try another image."}), 500
    except KeyError:
        error_message = f"AI response was valid JSON but was missing the 'records' key. AI Response: {response_text}"
        print(error_message)
        return jsonify({"error": "The AI response was structured incorrectly. Please try again."}), 500
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"error": "An unexpected server error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)