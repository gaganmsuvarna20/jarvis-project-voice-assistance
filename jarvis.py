import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import pyjokes
import webbrowser
import os

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        talk("Good morning")
    elif 12 <= hour < 18:
        talk("Good afternoon")
    else:
        talk("Good evening")
    talk("I am Jarvis, your voice assistant. How can I help you?")

def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = listener.listen(source)

    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        if 'jarvis' in command:
            command = command.replace('jarvis', '')
        print(f"You said: {command}")
    except sr.UnknownValueError:
        talk("Sorry, I didn’t catch that.")
        return ""
    return command

def run_jarvis():
    greet()
    while True:
        command = listen()

        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f'Current time is {time}')
        
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            talk(info)

        elif 'play' in command:
            song = command.replace('play', '')
            talk(f'Playing {song}')
            pywhatkit.playonyt(song)

        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
        
        elif 'joke' in command:
            talk(pyjokes.get_joke())

        elif 'open notepad' in command:
            os.system('start notepad.exe')

        elif 'stop' in command or 'exit' in command:
            talk("Goodbye!")
            break

        else:
            talk("Please say the command again.")

run_jarvis()

