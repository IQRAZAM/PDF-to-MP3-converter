# PDF to MP3 Converter

PDF to MP3 Converter is a Flask-based web application that allows users to upload PDF documents and convert them into MP3 audio files. The application extracts text from PDF files and converts it into speech, enabling users to listen to documents instead of reading them.

## Technologies Used

- Python
- Flask
- PyPDF2
- gTTS
- HTML
- CSS
- JavaScript
- Tailwind CSS

## Features

- Upload PDF files through a web interface
- Convert PDF text into MP3 audio
- Smooth progress bar with percentage display
- Automatic audio file download
- Simple and user-friendly interface

## Project Structure

PDF-to-MP3/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── uploads/ (created automatically)

## Installation and Setup

1. Clone the repository:
   git clone https://github.com/IQRAZAM/PDF-to-MP3-converter.git

2. Navigate to the project directory:
   cd PDF-to-MP3-converter

3. Create a virtual environment:
   python -m venv venv

4. Activate the virtual environment:
   - Windows:
     venv\Scripts\activate
   - Linux / Mac:
     source venv/bin/activate

5. Install dependencies:
   pip install -r requirements.txt

6. Run the application:
   python app.py

7. Open the application in a browser:
   http://127.0.0.1:5000

## Deployment

The application can be deployed on any platform that supports Python and Flask, such as PythonAnywhere. Upload the project files, create a virtual environment, install dependencies using requirements.txt, configure the WSGI file, and reload the web app.

## Use Cases

- Listening to study material
- Accessibility for visually impaired users
- Hands-free document consumption

## Future Enhancements

- Support for large PDF files
- Multiple language and voice support
- Improved audio controls
- Cloud storage integration

## License

This project is intended for educational purposes only.
