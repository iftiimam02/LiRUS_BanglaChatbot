from transformers import pipeline
from gtts import gTTS
import os

chatbot = pipeline("text2text-generation", model="model/fine_tuned_model")

def get_reply(text):
    response = chatbot(text)[0]["generated_text"]
    return response

def speak(text):
    filename = f"voice_cache/{hash(text)}.mp3"
    if not os.path.exists(filename):
        tts = gTTS(text=text, lang="bn")
        tts.save(filename)
    os.system(f"start {filename}")
