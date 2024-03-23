import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak out the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to convert speech to text
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I couldn't understand what you said.")
        query = None

    return query

# Function to greet the user
def greet():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    if hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

# Function to perform web search
def search(query):
    speak("Searching the web for " + query)
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# Function to open a website
def open_website(website_name):
    websites = {
        'google': 'https://www.google.com',
        'youtube': 'https://www.youtube.com',
        # Add more websites as needed
    }
    if website_name in websites:
        speak(f"Opening {website_name}")
        webbrowser.open(websites[website_name])
    else:
        speak("Sorry, I don't know how to open that website.")

# Function to play a random music file from a specified directory
def play_music(directory):
    music_files = [f for f in os.listdir(directory) if f.endswith('.mp3')]
    if music_files:
        music_file = os.path.join(directory, random.choice(music_files))
        os.system(f'start {music_file}')
    else:
        speak("No music files found in the specified directory.")

# Main function
def main():
    greet()
    speak("How can I assist you today?")

    while True:
        query = listen().lower()

        if query:
            if 'search for' in query:
                search_query = query.split('search for')[1].strip()
                search(search_query)
            elif 'open' in query:
                website_name = query.split('open')[1].strip()
                open_website(website_name)
            elif 'play music' in query:
                play_music("path/to/music/directory")
            elif 'exit' in query or 'quit' in query:
                speak("Goodbye!")
                break
            else:
                speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    main()
