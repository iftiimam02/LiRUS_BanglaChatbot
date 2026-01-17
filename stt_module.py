import speech_recognition as sr

def get_bangla_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("🎙️ মাইক: কিছু বলুন...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=7)
            text = r.recognize_google(audio, language="bn-BD")
            print("🗣️ আপনি বললেন:", text)
            return text
        except sr.WaitTimeoutError:
            print("শুনতে পারলাম না, আবার বলুন।")
            return ""
        except sr.UnknownValueError:
            print("শুনতে পারলাম না, আবার বলুন।")
            return ""
        except sr.RequestError:
            print("Google API error")
            return ""
