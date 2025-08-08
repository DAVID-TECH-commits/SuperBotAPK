import subprocess
import sys

try:
    import speech_recognition as sr
    recognizer = sr.Recognizer()
    print("Voice recognition module loaded successfully!")
except ImportError:
    print("SpeechRecognition not found. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "SpeechRecognition", "pyaudio"])
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        print("SpeechRecognition installed and loaded successfully!")
    except Exception as e:
        print(f"Installation complete but could not load speech recognition: {e}")
