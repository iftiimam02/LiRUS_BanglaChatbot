import sounddevice as sd
from scipy.io.wavfile import write

print("🎙️ বলুন কিছু (5 সেকেন্ড)...")
fs = 16000  # sample rate
seconds = 5

recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()
write("test.wav", fs, recording)
print("✅ রেকর্ডিং শেষ হয়েছে। এখন ফোল্ডারে test.wav ফাইল দেখুন।")
