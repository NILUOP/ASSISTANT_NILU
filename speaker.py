# speaker library

import pyttsx3

engine = pyttsx3.init()

 # takes input as string and speak it out
def speak(text):

    engine.say(text)
    engine.runAndWait()
