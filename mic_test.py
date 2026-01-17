import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("মাইক পরীক্ষা: কিছু বলুন...")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="bn-BD")
        print("আপনি বললেন:", text)
    except:
        print("শব্দ শনাক্ত করা যায়নি")
