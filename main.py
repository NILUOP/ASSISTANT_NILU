import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import requests
import os

import sounddevice as sd
import scipy.io.wavfile as wav
import whisper

from gtts import gTTS


recognizer = sr.Recognizer()
engine = pyttsx3.init()

duration = 5
samplerate = 16000

def speak(text):

    engine.say(text)
    engine.runAndWait()

def process_command(c):
    if "open google" in c.lower():
        wb.open("https://www.google.com")
    elif "open youtube" in c.lower():
        wb.open("https://www.youtube.com")
    elif "open chatgpt" or "open chat gpt" or "open chat g p t" in c.lower():
        wb.open("https://www.chatgpt.com")
    else:
        print("unknown command")


if(__name__ == "__main__"):
    speak("assistant nilu being ready")

    while True:
        duration = 5
        samplerate = 16000

        print("speak now...")

        recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
        sd.wait()
        print("✅ Recording complete!")

        audio_path = "my_voice.wav"
        wav.write(audio_path, samplerate, recording)

        model = whisper.load_model("medium")  # You can use 'tiny', 'small', etc.
        result = model.transcribe(audio_path)
        print(result["text"])

        process_command(result["text"])
        
        # except Exception as e:
        #     print("Error; {0}".format(e))