from flask import Flask, request, send_file, jsonify, render_template
from gtts import gTTS
import PyPDF2
import os
import time

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')  # Make sure your file is named 'index.html'

# Upload route
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.pdf'):
        pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(pdf_path)

        # Extract text
        text = extract_text_from_pdf(pdf_path)

        # Convert to MP3
        mp3_filename = file.filename.replace('.pdf', '.mp3')
        mp3_path = convert_text_to_mp3(text, mp3_filename)

        # Remove PDF after processing
        os.remove(pdf_path)

        # Send MP3 file
        return send_file(mp3_path, as_attachment=True, download_name=mp3_filename, mimetype='audio/mpeg')

    return jsonify({'error': 'Invalid file type'}), 400

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ''
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + '\n'
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""
    return text

# Convert text to MP3
def convert_text_to_mp3(text, filename):
    mp3_path = os.path.join(UPLOAD_FOLDER, filename)
    try:
        if not text.strip():
            tts = gTTS(text="No readable text found in the PDF.", lang='en')
        else:
            tts = gTTS(text=text, lang='en')
        tts.save(mp3_path)
    except Exception as e:
        print(f"Error converting text to MP3: {e}")
        with open(mp3_path, 'w') as f:
            pass
    return mp3_path

if __name__ == '__main__':
    app.run(debug=True)


