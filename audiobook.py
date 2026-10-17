import pyttsx3
import pypdf
import os

def pdf_to_audio(pdf_path, output_audio="lecture_audio.mp3"):
    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' not found.")
        return

    print("Reading PDF...")
    reader = pypdf.PdfReader(pdf_path)
    full_text = ""

    # Extract text from every page
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            full_text += text

    if not full_text.strip():
        print("Could not extract any text from the PDF.")
        return

    print(f"Extracted {len(full_text.split())} words. Converting to audio...")
    
    # Initialize text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)  # Reading speed (words per minute)

    # Save to audio file
    engine.save_to_file(full_text, output_audio)
    engine.runAndWait()
    print(f"Done! Audio file saved as '{output_audio}'.")

if __name__ == "__main__":
    file_name = input("Enter the name/path of your PDF file: ")
    pdf_to_audio(file_name)