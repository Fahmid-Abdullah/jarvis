
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import pyjokes
import requests
import shutil
import pywhatkit
from bs4 import BeautifulSoup
import requests
import win32com.client as wincl
from urllib.request import urlopen
import win32api
import win32con
import time

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 220)
engine.setProperty('volume', 2)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour <= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    print("I'm Jarvis. How can I help you sir?")
    speak("I'm Jarvis. How can I help you sir?")


def username():
    speak("What should I call you sir?")
    uName = takeCommand()
    speak("Nice to meet you")
    speak(uName)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uName.center(columns))
    print("#####################".center(columns))
     
    speak("How can I Help you, Sir?")


def takeCommand():
     
    r = sr.Recognizer()
     
    while True:
        with sr.Microphone() as source:
            print("Listening...\n")
            r.adjust_for_ambient_noise(source, duration=0.5)
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...\n")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query.lower()

        except Exception:
            print("...\n")

def pause_media():
    win32api.keybd_event(win32con.VK_MEDIA_PLAY_PAUSE, 0, 0, 0)
    win32api.keybd_event(win32con.VK_MEDIA_PLAY_PAUSE, 0, win32con.KEYEVENTF_KEYUP, 0)

if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    greetMe()
    flag = 1

    while True:
        while flag == 0:
            print("Say wake up Jarvis to begin...")
            query0 = takeCommand().lower()
            if "wake up jarvis" in query0 or "wake up jarvice" in query0:
                print("Booting up sir")
                greetMe()
                flag = 1
        if flag == 1:
            print("Listening...")
            query = takeCommand().lower()
            if "how are you" in query:
                speak("I am doing well sir. How are you?")
                query2 = takeCommand().lower()
                if "fine" in query2 or "well" in query2 or "good" in query2 or "okay" in query2:
                    if "not" in query2:
                        speak("Sorry to hear that sir.")
                    else:
                        speak("Glad to hear it sir")
            elif "who am i" in query:
                speak("You're a iron man fan boy sir")
            elif "who are you" in query or "what's your name" in query or "what is your name" in query:
                speak("I am jarvis version one point o sir")
            elif "who made you" in query:
                speak("I am a virtual assistant made to mimic jarvis from iron man")
            elif "wikipedia" in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 3)
                speak("Wikipedia says")
                print(results)
                speak(results)
                speak("Would you like to learn more?")
                query2 = takeCommand().lower()
                if "yes" in query2:                      
                    pywhatkit.search(query)
                speak("Understood.")
            elif "search" in query:
                query = query.replace("search", "")       
                webbrowser.open(query)
            elif "open youtube" in query:
                speak("Opening Youtube...\n")
                webbrowser.open("https://www.youtube.com")
            elif "open owl" in query:
                speak('Opening OWL\n')
                webbrowser.open("https://owl.uwo.ca/portal")
            elif "chat gpt" in query:
                speak("Opening ChatGPT\n")
                webbrowser.open("https://chat.openai.com")
            elif "search" in query:
                query = query.replace("search", "")       
                webbrowser.open(query)
            elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                speak("Locating ")
                speak(location)
                webbrowser.open("https://www.google.nl/maps/place/" + location)
            elif "time" in query:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The time is {strTime}. sir")
            elif "joke" in query:
                speak(pyjokes.get_joke())
            elif "look up" in query:
                query = query.replace("look up", "") # figure out dictionary
                webbrowser.open("https://www.dictionary.com/browse/" + query)
            elif "synonym" in query or "synonyms" in query or "antonym" in query or "antonyms" in query:
                query = query.replace("synonym", "")
                query = query.replace("synonyms", "")
                query = query.replace("antonym", "")
                query = query.replace("antonyms", "")
                webbrowser.open("https://www.thesaurus.com/browse/" + query)
            elif "play" in query:
                speak("Playing on YouTube\n")
                query = query.replace('play', '')
                pywhatkit.playonyt(query)
            elif "sleep" in query:
                print("Going into sleep mode.")
                speak("Going into sleep mode.")
                flag = 0
            elif "media" in query:
                pause_media()
            elif "exit" in query or "quit" in query or "goodbye" in query:
                speak('Goodbye sir\n')
                sys.exit(0)

        
