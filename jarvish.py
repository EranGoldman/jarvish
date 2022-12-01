import pyttsx3                            ## "pyttsx3" is a text-to-speech conversion library in Python. (offline)
import datetime                           ##  Builten librabary in python for date time operation.
import speech_recognition as sr           ##  Machine's ability to listen to spoken words and identify them
import wikipedia                          ##  wikipedia
import webbrowser                         ##  Builten librabary for web related task
import os                                 ##  Builten librabary for operating sysytem
import smtplib                            ## it is use for acess the email through google

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")

##setting the voice
engine.setProperty('voice',voices[0].id)   ##cooseing the devid voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour <12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        
    else:
        speak("Good evening")
    
    speak("I am jarvish Sir. Please tell me how may I help you")
    

def takeCommand():
    """
    it take speech through microphone from user 
    and return string output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1   ## it give time for take input as voice
        audio = r.listen(source)  
    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        # print(e)
        print("Say that again please..")
        return "None"
    return query

## we need to go to google an anable the less secure app 
# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('your@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case  
        
        
        # Logic for exacuting task based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("Acording to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            speak("why not sir")
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            speak("why not sir")
            webbrowser.open("google.com")
              
        elif 'open stackoverflow' in query:
            speak("why not sir")
            webbrowser.open("stackoverflow.com")
            
        elif 'play music' in query:
            music_dir = "D:\\SONGS"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
            
        elif 'open code' in query:
            codePath = "C:\\Users\\AJIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile (codePath)
        
        # elif "email to ajit" in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "harryyourEmail@gmail.com"    
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend harry bhai. I am not able to send this email")
        
        