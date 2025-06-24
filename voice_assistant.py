import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pywhatkit

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Speak out text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Greet user based on time
def greet_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I help you?")

# Return current time
def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}")

# Return current date
def tell_date():
    date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {date}")

# Web search on Google
def google_search(query):
    speak(f"Searching Google for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

# Search on Wikipedia
def wikipedia_search(query):
    speak("Searching Wikipedia")
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except Exception:
        speak("Sorry, I couldn't find anything on Wikipedia.")

# Play video on YouTube
def youtube_search(query):
    speak(f"Playing {query} on YouTube")
    pywhatkit.playonyt(query)

# Recognize voice input
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("User said:", command)
    except:
        speak("Sorry, I did not catch that.")
        return ""
    return command.lower()

# Main function
def run_assistant():
    greet_user()
    while True:
        query = take_command()

        if "time" in query:
            tell_time()

        elif "date" in query:
            tell_date()

        elif "google" in query:
            search_term = query.replace("google", "").strip()
            google_search(search_term)

        elif "wikipedia" in query:
            topic = query.replace("wikipedia", "").strip()
            wikipedia_search(topic)

        elif "youtube" in query or "play" in query:
            video = query.replace("youtube", "").replace("play", "").strip()
            youtube_search(video)

        elif "stop" in query or "exit" in query:
            speak("Goodbye!")
            break

        elif query != "":
            speak("Please try again with a different command.")


if __name__ == "__main__":
    run_assistant()
