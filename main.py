import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import subprocess
import requests
import os
import time

import sounddevice as sd
import scipy.io.wavfile as wav
import whisper

import multiprocessing as mp

import recorder
import transcriber
import speaker
import command_processor

from gtts import gTTS


if(__name__ == "__main__"):
    speaker.speak("Assistant Nilu is ready.")
    counter = 0

    while True:
        try:
            audio_path = recorder.record(counter)
            result = transcriber.transcribe(audio_path)
            counter += 1
            if "hello" in result.lower():
                print("hotword found!!")
                speaker.speak("ready to take command")
                audio_path = recorder.record(counter)
                command = transcriber.transcribe(audio_path)
                counter += 1

                command_processor.process_command(command)

            time.sleep(1)  # Optional pause
        except KeyboardInterrupt:
            print("🛑 Exiting...")
            break
        except Exception as e:
            print("⚠️ Error:", e)
            time.sleep(1)
