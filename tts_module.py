import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # speaking speed

# Pick a male voice (usually David or Male)
voices = engine.getProperty('voices')
for v in voices:
    if 'male' in v.name.lower() or 'david' in v.name.lower():
        engine.setProperty('voice', v.id)
        break

def speak_bangla(text):
    engine.say(text)
    engine.runAndWait()
