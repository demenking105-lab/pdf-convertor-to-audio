# 🎧 PDF-to-Audiobook Converter

A lightweight Python tool that extracts text from PDF documents (such as lecture notes, articles, or research papers) and converts them into offline MP3 audiobooks.

## 🚀 Features
- **Automated Text Extraction**: Reads multi-page PDFs cleanly using `pypdf`.
- **Text-to-Speech (TTS)**: Synthesizes natural speech using the offline `pyttsx3` engine.
- **Custom Speech Rate**: Configured reading speed (160 WPM) optimized for studying.
- **Offline & Private**: Converts documents completely locally without uploading files to any third-party servers.

## 🛠️ Built With
- **Python 3**
- `pyttsx3` (Offline Text-to-Speech library)
- `pypdf` (PDF processing and text extraction)

## 💻 How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/pdf-to-audiobook.git
   cd pdf-to-audiobook
2. pip install pypdf pyttsx3
3. python audiobook.py
