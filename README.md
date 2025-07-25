# Image to Excel Converter
<img width="1920" height="1072" alt="home" src="https://github.com/user-attachments/assets/2d36fca0-1ab4-4805-8998-6cd3aa089014" />
This web application allows users to upload an image of a handwritten table/ledger and convert it into an Excel file. Requires user's own Gemini API key.

## MORE CONSISTENT THAN OCR BASED SOLUTION. USES GEMINI'S LATEST 2.5 FLASH MODEL. COMPATIBLE WITH DIFFERENT TYPES OF HANDWRITING BUT TRY TO KEEP IT CLEAN AND HAVE PROPER DEFINED ROWS AND COLUMNS

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
## EXAMPLES
<img width="885" height="512" alt="image" src="https://github.com/user-attachments/assets/c4e430de-7f2f-494d-9341-fc1cc97bdbe7" />




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

## 📜 License  
© 2025 Mriganka Baishya. All rights reserved.

This repository and its contents are protected by copyright law and international treaties.
Unless otherwise stated, no part of this codebase may be copied, reproduced, distributed, modified, or used in any form without the prior written consent of the copyright holder.

❌ Unauthorized use is strictly prohibited and may result in legal action.

This project is provided for educational and reference purposes only.
Commercial or non-commercial reuse, redistribution, or derivation is not permitted under any circumstances.

If you wish to request permission to use this code, please contact the author directly.
