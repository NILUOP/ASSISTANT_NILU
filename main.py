import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import subprocess
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

brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

profile1 = "Profile 1" # --> gaming
profile2 = "Profile 2" # --> nisargkumar (profectional)
profile3 = "profile 3" # --> college
profile4 = "Default" # --> nisarg


def speak(text):

    engine.say(text)
    engine.runAndWait()

def process_command(c):
    if "open google" in c.lower():
        wb.open("https://www.google.com")

    elif "open youtube" in c.lower() or "open you tube" in c.lower():
        wb.open("https://www.youtube.com")

    elif "open chatgpt" in c.lower() or "open chat gpt" in c.lower():
        wb.open("https://www.chatgpt.com")

    elif "open linkedin" in c.lower() or "open linked in" in c.lower() or "open link in" in c.lower():
        subprocess.Popen([brave_path, f"--profile-directory={profile2}", "https://www.linkedin.com"])
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

        if(result["text"] != ""):
            process_command(result["text"])
            break
        
        # except Exception as e:
        #     print("Error; {0}".format(e))