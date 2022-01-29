from pip import main
import smtplib
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0) and hour<12:
        speak("Good Morning!'")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello Sir I am Jarvis your Virtual Assistant,How may I help you")

def takeCommand():
    #It takes microphone input from the user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        # print(e)     
        print("Say that again please...")
        return "None"
    return query

# def sendEmail(to,content):
#     server=smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('202011012@diu.iiitvadodara.ac.in',202011012)
#     server.sendmail('202011012@diu.iiitvadodara.ac.in',to,content)
#     server.close()

if __name__ == "__main__":
    wishMe()
    #Logic for executing the tasks based on the query
    while 1:
       query=takeCommand().lower()
       if 'wikipedia' in query:
           speak("Searching results on wikipedia")
           query=query.replace("wikipedia","")
           results=wikipedia.summary(query,sentences=2)
           speak("According to Wikipedia")
           print(results.encode("utf-8"))
           speak(results)
       
       elif 'open google' in query:
           webbrowser.open("google.com")

       elif 'open chrome' in query:
           webbrowser.open("chrome.com") 

       elif 'open youtube' in query:
           webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=21s")

       elif 'open stackoverflow' in query:
           webbrowser.open("stackoverflow.com")
       
       elif 'best british youtube' in query:
           webbrowser.open("https://www.youtube.com/watch?v=U3aDL6zUPPQ")

       elif 'play music' in query:
           music_dir='C:\\Users\\ARORA\\Music\\Songs'
           songs=os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir,songs[1]))

       elif 'thank you' in query:
           speak("Your Welcome!")

       elif 'the time' in query:
           strTime=datetime.datetime.now().strftime("%H hours %M minutes & %S seconds")
           speak(f"Sir, the time is{strTime}")
        
       elif 'open code' in query:
           codePath = "C:\\Users\\ARORA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)

       # elif 'email to Ishaan':
       #     try:
       #         speak("What should I say Sir?")
       #         content=takeCommand()
       #         to="aroraishaan2002@gmail.com"
       #         sendEmail(to,content)
       #         speak("Email has been sent!")
       #     except Exception as e:
       #         print(e)
       #         speak("Sorry I am not able to send this email")
