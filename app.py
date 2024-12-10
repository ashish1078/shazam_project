import speech_recognition as sr
from langdetect import detect
from googleapiclient.discovery import build
import webbrowser

# Set up the YouTube Data API
API_KEY = "AIzaSyDarhyok-vNAKD1XAxY7VNmKKqhmVnSAYo"
youtube = build("youtube", "v3", developerKey=API_KEY)

# Function to listen to speech and convert to text
def listen_to_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)
        
    try:
        # Convert speech to text
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

# Function to detect the language of the speech
def detect_language(text):
    try:
        language = detect(text)
        print(f"Detected language: {language}")
        return language
    except Exception as e:
        print(f"Error in language detection: {e}")
        return None

# Function to search YouTube for songs related to the detected text
def search_youtube(query):
    request = youtube.search().list(
        part="snippet",
        maxResults=5,
        q=query + " song"
    )
    
    response = request.execute()
    
    video_urls = []
    for item in response['items']:
        video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        video_urls.append(video_url)
    
    return video_urls

# Main function to execute the project
def main():
    # Step 1: Listen to speech and convert to text
    text = listen_to_speech()
    if text is None:
        return
    
    # Step 2: Detect language of the text
    language = detect_language(text)
    if language is None:
        return
    
    # Step 3: Search YouTube for related songs
    video_urls = search_youtube(text)
    
    if not video_urls:
        print("No related songs found on YouTube.")
    else:
        print("Found the following related songs on YouTube:")
        for url in video_urls:
            print(url)
            webbrowser.open(url)  # Opens the YouTube video in the browser

if __name__ == "__main__":
    main()
