import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    try:
        tts = gTTS(text=text, lang='bn')
        filename = "response.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
    except:
        engine.say(text)
        engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ বলুন...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="bn-BD")
        print(f"🗣️ আপনি বললেন: {text}")
        return text
    except sr.UnknownValueError:
        print("🤖: দুঃখিত, আমি বুঝতে পারিনি।")
        return None
    except sr.RequestError:
        print("🤖: ইন্টারনেট সংযোগে সমস্যা আছে।")
        return None

def main():
    print("LiRUS চালু হয়েছে। (বলুন 'বন্ধ' বলতে বন্ধ হবে)")
    while True:
        user_input = listen()
        if not user_input:
            continue
        if "বন্ধ" in user_input:
            speak("চলতি সেশন শেষ করা হল।")
            print("🤖: চলতি সেশন শেষ করা হল।")
            break
        response = f"আপনি বললেন: {user_input}"
        speak(response)

if __name__ == "__main__":
    main()
