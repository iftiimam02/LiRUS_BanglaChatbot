# app.py
from flask import Flask, render_template, request, jsonify, send_file
from bangla_ml_chatbot import get_reply, text_to_speech_bangla
import os

app = Flask(__name__)
VOICE_CACHE = "voice_cache"
os.makedirs(VOICE_CACHE, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")  # your existing index.html

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_message = data.get("message", "")
    reply_text = get_reply(user_message)

    # Generate TTS
    audio_path = text_to_speech_bangla(reply_text)
    audio_url = f"/voice/{os.path.basename(audio_path)}"

    return jsonify({"reply": reply_text, "audio_url": audio_url})

@app.route("/voice/<filename>")
def serve_audio(filename):
    path = os.path.join(VOICE_CACHE, filename)
    if os.path.exists(path):
        return send_file(path, mimetype="audio/mpeg")
    return "File not found", 404

if __name__ == "__main__":
    app.run(debug=True)
