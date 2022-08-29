import datetime ## Importing Relevant Libraries
import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
from PyDictionary import PyDictionary
import wikipedia
import spotify
import pyjokes
dictionary = PyDictionary() ##making an object of PyDictionary library
listener = sr.Recognizer()  ## intializing speech-recognition library
engine = pyttsx3.init()     ## Initializing python text to speech library
voices = engine.getProperty('voices') ## Getting built-in voices
engine.setProperty('voice', voices[1].id) ## Setting the voice to the female
def talk(text): ## this function will be called whenever we want our Assitant to say anything
    engine.say(text)
    engine.runAndWait()

##We will use try except block for this program so if any error occurs, the program is terminated
try:
    with sr.Microphone() as source: #Setting Microphonr as source for commands
        print("listening")
        voice = listener.listen(source) ## in the next 3 lines, I am taking commands from the user through microphone
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command: ## if we say siri instead of alexa, the speech will not work
            command = command.replace('alexa', '')
        if 'play' in command: ## If block for asking alexa to play something on Youtube
            play = command.replace('play ', '')
            talk('opening '+play)
            pywhatkit.playonyt(play)
            print(play)
        elif 'time' in command: ## if block to ask alexa for the time
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('current time is: ' + time)
            print(time)
        elif 'who is ' in command: ## if block to ask alexa about a personality on wikipedia
            person = command.replace('who is ', '')
            info = wikipedia.summary(person, 1)
            talk(info)
            print(info)
        elif 'what is the meaning of ' in command: ## if block to ask alexa meaning of a word
            word = command.replace('what is the meaning of ', '')
            mean = dictionary.meaning(word)
            print(mean)
            talk(mean)
        elif 'joke' in command: #if block to ask alexa to tell a jokw
            talk(pyjokes.get_joke())
except:
    pass
