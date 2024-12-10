from speech_recognition_util import recognize_speech  # Import your function from your utility file
from language_detection import detect_language       # Import your language detection function
from youtube_search import search_youtube           # Import your YouTube search function

def main():
    # Step 1: Capture speech and recognize text
    text = recognize_speech()
    print(f"Recognized Text: {text}")

    # Step 2: Detect the language of the text
    language = detect_language(text)
    print(f"Detected Language: {language}")

    # Step 3: Search YouTube for songs related to the text
    videos = search_youtube(text)
    print(f"Found Videos: {videos}")

if __name__ == "__main__":
    main()
