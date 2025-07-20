# Image to Excel Converter

This web application allows users to upload an image of a handwritten table/ledger and convert it into an Excel file. Requires user's own Gemini API key.  

## Features

- **Image Upload:** Supports JPG and PNG image formats.
- **Drag and Drop:** Easily drag and drop image files for upload.
- **Data Extraction:** Uses the Google Gemini API to extract tabular data from images.
- **Excel Conversion:** Converts the extracted data into an Excel (.xlsx) file using Python and pandas.
- **User-Friendly Interface:** Simple and intuitive web interface with Home, About, and How it Works pages.

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **APIs:** Google Gemini API
- **Libraries:**
    - `pandas`: For data manipulation and Excel file creation.
    - `Pillow`: For image processing.
    - `python-dotenv`: For managing environment variables.
<img width="1920" height="1072" alt="home" src="https://github.com/user-attachments/assets/2d36fca0-1ab4-4805-8998-6cd3aa089014" />

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    Run the `install_requirements.bat` file by double-clicking it, or run the following command in your terminal:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your API Key:**
    -   Rename the `.env.example` file to `.env`.
    -   Open the `.env` file and add your Google Gemini API key:
        ```
        GEMINI_API_KEY=YOUR_API_KEY
        ```

5.  **Run the application:**
    ```bash
    python app.py
    ```

6.  **Access the application:**
    Open your web browser and go to `http://127.0.0.1:5000`.

## How It Works

1.  **Upload Image:** The user uploads an image containing a table.
2.  **API Request:** The frontend sends the image to the Flask backend.
3.  **Gemini API:** The backend sends the image to the Google Gemini API for data extraction.
4.  **JSON to Excel:** The structured JSON response from the API is converted into a pandas DataFrame and then saved as an Excel file.
5.  **Download:** The server sends the Excel file back to the user for download.
