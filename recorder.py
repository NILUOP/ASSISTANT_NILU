import sounddevice as sd
import scipy.io.wavfile as wav

samplerate = 16000
duration = 5

def record(counter):
    print("🎙️ Speak now...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    print("✅ Recording done!")

    audio_path = f"audio_{counter}.wav"
    wav.write(audio_path, samplerate, recording)
    return audio_path
