import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

# Initialize engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use female voice

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant. How can I help you today?")

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.pause_threshold = 1
        audio = listener.listen(source)

    try:
        print("Recognizing...")
        query = listener.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except sr.UnknownValueError:
        speak("Sorry, I did not get that. Please say it again.")
        return "None"
    return query.lower()

def run_alexa():
    wish_user()
    while True:
        query = take_command()

        if "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia:")
            speak(result)

        elif "open youtube" in query:
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            webbrowser.open("https://google.com")

        elif "stop" in query or "exit" in query:
            speak("Okay, shutting down. Have a nice day!")
            break

if __name__ == "__main__":
    run_alexa()
