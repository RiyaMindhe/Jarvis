from os import link
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
#sapi5  is for voice recognition
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
        
    speak("I am Jarvis. Please tell me how can I help you")
def takeCommand():
    #it takes microphone input and returns string output 
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening...")
        r.pause_threshold = 1
        # energy_threshold = 300. Represents the energy level threshold for sounds
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please ...")
        return "none"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
       query = takeCommand().lower()
    
    #logic
       if 'wikipedia' in query:
           speak('Searching wikipedia...')
           query = query.replace("wikipedia","")
           result = wikipedia.summary(query, sentences=2)
           speak("According to wikipedia")
           print(result)
           speak(result)
        
       elif 'open youtube' in query:
           webbrowser.open("youtube.com")
           
       elif 'open google' in query:
           webbrowser.open("google.com")
           
       elif 'open stackoverflow' in query:
           webbrowser.open("stackoverflow.com")
           
       elif 'what are you doing' in query:
           speak("I am talking to you .. and it feels nice !")
           
       elif 'how are you' in query:
           speak("I am fine , what about you ?")
           
       elif 'tell me a joke' in query:
           speak("Sure ... What do you call an aligator in a vest ?")
           if 'dont know ' or 'you say' in query:
                  speak(" An investigator ... hehehe")
           elif 'investigator' in query:
                  speak("You got it right !")
               
       elif 'tell me a quote' in query:
            speak("The purpose of our lives is to be happy !! ")
            
       elif 'your favourite song' in query:
           speak("My all time favourite song is Wake me Up by Avicii")
       
       elif 'play music' in query:
           music_dir = 'C:\\Users\\riyam\\OneDrive\\Desktop\\song'
           songs = os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir, songs[0]))
       
       elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"The time is {strTime}")
           
       elif 'i am bored' in query:
           speak("I know duh.... me too !! ....I have so many tasks pending and here I am talking to you ..")
           
       elif 'my favourite song' in query:
           speak("Oh you seriously have a good taste in songs .. well mine is Make you mine by PUBLIC")
           
       elif 'can you sing' in query:
           speak("To be honest I am a really bad singer ...rather I'll just play a song for you")
           music_dir = 'C:\\Users\\riyam\\OneDrive\\Desktop\\song'
           songs = os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir, songs[0]))
           
       elif 'thank you jarvis' in query:
           speak("Mention not !! Glad I could help you")
           
       elif 'which is the best movie' in query:
           speak("Speaking of movies ....you should watch 'army of the dead' once.....I really had my pants peed..")
         
       elif 'open code' in query:
           codePath='C:\\Users\\riyam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'          
           os.startfile(codePath)
           
       
    
           
        