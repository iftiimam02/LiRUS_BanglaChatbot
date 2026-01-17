from stt_module import get_bangla_speech
from nlp_module import bangla_reply
from tts_module import speak_bangla

def run_chatbot():
    print("LiRUS চালু হয়েছে। (বলুন 'bondho' বা 'বিদায়' বলতে বন্ধ হবে)")
    while True:
        user_input = get_bangla_speech()
        if user_input in ["bondho", "বিদায়", "বাই"]:
            speak_bangla("বিদায়! আবার দেখা হবে।")
            break
        if user_input.strip() == "":
            continue  # skip empty recognition
        reply = bangla_reply(user_input)
        print("🤖:", reply)
        speak_bangla(reply)

if __name__ == "__main__":
    run_chatbot()
