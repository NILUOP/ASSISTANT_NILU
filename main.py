# main file

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
from gtts import gTTS

# importing local libraries (files)
import recorder
import transcriber
import speaker
import command_processor



if(__name__ == "__main__"):
    speaker.speak("Assistant Nilu is ready.")
    counter = 0

    while True:
        try:
            audio_path = recorder.record(counter,5) # record voice
            result = transcriber.transcribe(audio_path) # transcrive the voice
            counter += 1

            if "hello" in result.lower(): # first hotword to give command
                print("hotword found!!")
                speaker.speak("ready to take command")
                audio_path = recorder.record(counter,8) # record command duration 8 seconds
                command = transcriber.transcribe(audio_path) # transcribe the command
                counter += 1

                command_processor.process_command(command) # process the command
            
            elif "stop" in result.lower(): # second hotword to stop the program
                break

            time.sleep(2)  # Optional pause

        except KeyboardInterrupt: # keyboard interrupt - second way to stop execution
            print("🛑 Exiting...")
            break

        except Exception as e: # exception handeling
            print("⚠️ Error:", e)
            speaker.speak("an error occured")
            time.sleep(1)
