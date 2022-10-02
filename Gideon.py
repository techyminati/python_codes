import pyttsx3  
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

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
        speak("Good Evening!")  

    speak("I am Gideon master . Please tell me how may I help you")



def telltime():



    time = str(datetime.datetime.now())

     

    print(time)

    hour = time[11:13]

    min = time[14:16]

    speak ("The time is sir" + hour + "Hours and" + min + "Minutes")


def tellday():

    Day_dict = {1: 'Monday', 2: 'Tuesday',

                3: 'Wednesday', 4: 'Thursday',

                5: 'Friday', 6: 'Saturday',

                7: 'Sunday'}

     

    for day in Day_dict.keys():

        day_of_the_week = Day_dict[day]

        print(day_of_the_week)

        speak("The day is " + day_of_the_week)



def Hello():


    speak ("hello sir I am your desktop assistant,My name is gideon, Tell me how may I help you ")


def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
    
        print("Say that again please...") 
        speak ("couldn't recognize it say that again please") 
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Sender's Mail', 'pass')
    server.sendmail('sender's mail', to,)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

    
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        if 'youtube' in query:
            speak('opening youtube....')
            content=takeCommand

        if 'google' in query:
            speak('opening google...')
            content=takeCommand

        if 'spotify'in query:
            speak('opening spotify')
            content=takeCommand
        
        if 'stack overflow'in query:
            speak('oepning stack overflow')
            content=takeCommand

    
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'open spotify' in query:
            webbrowser.open("spotify.com") 

        elif 'the time' in query:
            telltime()
        
        elif "which day it is" in query:
            tellday()


        elif "tell me the time" in query:

            telltime()

        elif "Hello" in query:
            
            Hello()

        elif"terminate" in query:
            speak("Terminating the session, bye master")
            exit()

        elif 'exit' in query:
            
            exit()
        

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "EMail"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Couldnot send due to some problem. My apologies sir")   
