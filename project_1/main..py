import speech_recognition as sr 
import pyttsx3

recognixer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
     speak("Hello, I am your assistant. How can I help you?") 