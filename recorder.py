# recorder library

import sounddevice as sd
import scipy.io.wavfile as wav

samplerate = 16000

 # takes 2 input counter for the number of audio file, and duration for how long the recorded audio file is gonna be
def record(counter,duration):
    print("🎙️ Speak now...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16') # recording the file
    sd.wait()
    print("✅ Recording done!")

    audio_path = f"audio_{counter}.wav" # name it according to counter
    wav.write(audio_path, samplerate, recording) # save it in the same folder as the all other files
    return audio_path # return the path or name of the audio file
