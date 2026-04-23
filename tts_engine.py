from gtts import gTTS
import os

def text_to_audio(text, filename):
    path = f"../uploads/{filename}.mp3"
    tts = gTTS(text=text, lang='en')
    tts.save(path)
    return path