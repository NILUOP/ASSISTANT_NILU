# transcriber library

import whisper
import os

model = whisper.load_model("medium").to("cuda")

# takes audio file as input and returns string of text
def transcribe(audio_path):
    print(f"🔎 Transcribing {audio_path}...")
    result = model.transcribe(audio_path, language="en")
    print(f"📝 Transcription: {result['text']}")

    os.remove(audio_path) # also removes given audio file
    return result["text"]
