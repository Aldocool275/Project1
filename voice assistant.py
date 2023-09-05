import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

assname=("Alexa")
def wishMe():
    hour=int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<16:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    
    assname=("Alexa")
    speak("I am your assistant")
    speak(assname)

def takeCommand():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing")
        query=r.recognize_google(audio,language="en-in")
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice")
        speak("Unable to recognize your voice")
    
    return query

def username():
    speak("What should I call you sir?")
    uname=takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns=shutil.get_terminal_size().columns
    print("Welcome Mr.",uname.center(columns))
    speak("How can I help you,Sir?")

if __name__=="__main__":
    clear=lambda:os.system("cls")
    clear()
    wishMe()
    username()

    while True:
        query=takeCommand().lower()

        if "open youtube" in query:
            speak("Here you go to Youtube")
            webbrowser.open("youtube.com")
        elif "open google" in query:
            speak("Here you go to Google")
            webbrowser.open("google.com")
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("% H:% M:% S")
            speak("The time is",strTime)
        elif "how are you" in query:
            speak("I am fine,Thank You")
            speak("How are you,Sir")
        elif "fine" in query:
            speak("It's good to know that you are fine")
        elif "what's your name" in query:
            speak("My friends call me")
            speak(assname)
        elif "who made you" in query:
            speak("I have been made by Aldous")
        elif "joke" in query:
            speak(pyjokes.get_joke())
        elif "calculate" in query:
            app_id="Wolframalpha api id"
            client=wolframalpha.Client(app_id)
            indx=query.lower().split().index("calculate")
            query=query.split()[indx+1:]
            res=client.query(''.join(query))
            answer=next(res.results).text
            speak("The answer is",answer)
        elif "who I am" in query:
            speak("If you talk then definitely you are a human")
        elif "why you came to this world" in query:
            speak("Thanks to Aldous,he created me as a college project")
        elif "who are you" in query:
            speak("I am your virtual assistant")
        elif "news" in query:
            try:
                jsonObj=urlopen("https://timesofindia.indiatimes.com/?from=mdr")
                data=json.load(jsonObj)
                i=1

                speak("Here are some news from Times Of India")
                print("========TIMES OF INDIA========")

                for item in data["articles"]:
                    print(str(i)+"."+item["title"]+"\n")
                    print(item["description"]+"\n")
                    speak(str(i)+"."+item["title"]+"\n")
                    i+=1
            except Exception as e:
                print(str(e))
        elif "camera" or "click a picture" in query:
            ec.capture(0,"Alexa Camera","img.jpg")
        elif "hibernate" or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown/h")
        elif "Alexa" in query:
            wishMe()
            speak("Alexa in your service")
        elif "weather" in query:
            api_key="Api key"
            base_url="https://weather.com/en-IN/weather/tenday/l/Mandrem+Goa?canonicalCityId=e0b0b52c3e1358c6b56835451a3d5cc3fd9362bc2aef41795d44381c3cdd511f"
            speak("City Name:")
            print("City Name:")
            city_name=takeCommand()
            complete_url=base_url+"appid"+api_key+"&q"+city_name
            response=requests.get(complete_url)
            x=response.json()

            if x["code"]!="404":
                y=x["main"]
                current_temp=y["temp"]
                z=x["weather"]
                weather_description=z[0]["description"]
                print("Temperature:",str(current_temp))
                speak("The temperature is",str(current_temp))
            else:
                speak("City not found")
        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
        elif "Good Morning" in query:
            speak("A warm"+query)
            speak("How are you sir")

