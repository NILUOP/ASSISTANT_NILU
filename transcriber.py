import whisper
import os

model = whisper.load_model("medium").to("cuda")

def transcribe(audio_path):
    print(f"🔎 Transcribing {audio_path}...")
    result = model.transcribe(audio_path, language="en")
    print(f"📝 Transcription: {result['text']}")

    os.remove(audio_path)
    return result["text"]
