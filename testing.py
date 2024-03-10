import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition 
import datetime
import wikipedia 
import webbrowser
import os
import random as rand
import pywhatkit as kit
import ast
import win32api
import sys
import json, requests
import PyPDF2
import pyaudio 
import openai
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good evening!")  

    speak("I am Ashria Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 1000
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'quit' in query:
            engine.say("Quitting Sir, Thanks for using")
            print("Quitting Sir Thanks for using")
            engine.runAndWait()
            break

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open notepad' in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            tc = takeCommand().lower()
            if 'close it' in tc:
                speak('sure sir')
                os.system('taskkill /f /im notepad.exe')

        elif 'open command prompt' in query:
            os.system("start cmd")
            tc = takeCommand().lower()
            if 'close it' in tc:
                speak("sure sir")
                os.system('taskkill /f /im cmd.exe')
                
        elif 'open google' in query:
            # chr = os.system('start chrome')
            webbrowser.open("google.com")
            speak("sure sir, what should I search.")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = "c:\\Users\\sehga\\Music"
            songs = rand.choice(os.listdir(music_dir))
            print(songs)    
            os.startfile(os.path.join(music_dir, (songs)))
          
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif 'send message' in query:
            speak("To whom you want to send the message")
            nm = takeCommand().lower()
            with open('contacts.txt') as f:
                data = f.read()
            d = ast.literal_eval(data)
            if nm in d:
                print("contact found sir, please tell your message")
                speak("contact found sir, please tell your message")
                mssg = takeCommand().lower()
                hr = int(datetime.datetime.now().hour)
                mint = int(datetime.datetime.now().minute) + 2
                kit.sendwhatmsg(d[nm], mssg, hr, mint)
                speak("sir, message has been sent successfully")
            else:
                print("sorry sir, contact not found")
                speak("sorry sir, contact not found")

        elif 'open youtube' in query:
            speak("What you wanna play, sir??")
            sg = takeCommand().lower()
            kit.playonyt(sg)
            kit.pause(sg)
            speak(f"playing {sg} on youtube")
        
        elif 'set alarm' in query:
            nn = int(datetime.datetime.now().hour)
            if (nn == 6):
                music_dir = "c:\\Users\\sehga\\Music"
                alm = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, alm))
            speak("Alarm has been set successfully")

        elif 'the weather forecast' in query:
            print("Sir, please tell the name of city!")
            speak("Sir, please tell the name of city!")
            api_key = "ab800727f6761442617f49a0d6a9eb67"

            # The city and country code you want to retrieve the weather for
            city = takeCommand().lower()

            # The URL for the OpenWeatherMap API endpoint
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

            # Make a request to the API
            response = requests.get(url)

            # Convert the response to JSON
            data = json.loads(response.text)

            # Retrieve the weather information
            weather = data["weather"][0]["description"].title()
            temperature = round(data["main"]["temp"] - 273.15, 1)
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            wind_direction = data["wind"]["deg"]

            # Print the weather forecast
            print(f"The weather in {city} is {weather}.")
            speak(f"The weather in {city} is {weather}.")
            
            print(f"The temperature is {temperature}°C.")
            speak(f"The temperature is {temperature}°C.")

            print(f"The humidity is {humidity}%.")
            speak(f"The humidity is {humidity}%.")

            print(f"The wind speed is {wind_speed} m/s.")
            speak(f"The wind speed is {wind_speed} m/s.")

            print(f"The wind direction is {wind_direction}°.")
            speak(f"The wind direction is {wind_direction}°.")

        elif 'close notepad' in query:
            speak("sure sir.")
            os.system('taskkill /f /im notepad.exe')

        elif 'close command prompt' in query:
            speak("closing sir")
            os.system('taskkill /f /im cmd.exe')

        elif 'shutdown the pc' in query:
            speak('Are you sure sir??')
            ask = takeCommand().lower()
            if ask == 'yes':
                print("shutting down sir")
                speak("shutting down sir")
                os.system("shutdown /s /t 5")
            else:
                speak('sure sir, is there anything you want me to do??')      
        elif 'restart this pc' in query:
            speak('Are you sure sir, you want to restart??')
            ask = takeCommand().lower()
            if ask == "yes":
                speak("Restarting sir")
                os.system("shutdown /r /t 1")
            else:
                speak('sure sir, is there anything you want me to do??')
        
        # elif 'human interaction mode' in query:
        #     openai.api_key = 'sk-...VHz3'
        #     speak("Sure, what would you like to ask OpenAI?")
        #     user_input = takeCommand().lower()

        #     # Call the OpenAI GPT API
        #     response = openai.Completion.create(
        #         engine="text-davinci-003",
        #         prompt=user_input,
        #         max_tokens=150
            # )
        elif 'read pdf' in query:
            speak("tell the name of the file u want me to read")
            tc = takeCommand().lower()
            print(f"user said: {tc}")
            fN = tc+'.pdf'
            drives = win32api.GetLogicalDriveStrings()
            drives = drives.split('\000')[:-1]

            # search for the file in the root directory of each available drive
            found = False
            for drive in drives:
                root = os.path.join(drive, "\\")
                for dirpath, dirnames, filenames in os.walk(root):
                    if fN in filenames:
                        filepath = os.path.join(dirpath, fN)
                        print(f"File found at {filepath}")
                        with open(filepath, "rb") as f:
                            pdf_reader = PyPDF2.PdfReader(f)

                            # print the number of pages in the PDF file
                            print(f"Number of pages: {len(pdf_reader.pages)}")

                            # loop through each page in the PDF file and print its text content
                            for i in range(len(pdf_reader.pages)):
                                page = pdf_reader.pages[i]
                                text = page.extract_text()
                                print(f"Page {i+1}:\n{text}\n")
                                speak(f"Page {i+1}:\n{text}\n")
                                found = True
                                break                
                if found:
                    break

            else:
                print(f"File not found on any drive")
                speak(f"File not found on any drive")

    
                