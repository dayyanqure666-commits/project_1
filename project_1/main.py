import os
import musiclib
import speech_recognition as sr 
import pyttsx3
#import pyaudio 


engine = pyttsx3.init()# Initialize the text-to-speech engine

def speak(text):# Function to convert text to speech
    engine.say(text)
    engine.runAndWait()
def process_command(command):# Function to process the voice command
    command = command.lower()
    if "hello" in command:
        speak("Hello, how can I help you?")
    elif "what is your name" in command:
        speak("My name is Jarvis.")
    elif "open google" in command:
        os.system("start chrome https://www.google.com")
    elif "open youtube" in command:
        os.system("start chrome https://www.youtube.com")
    elif "open facebook" in command:
        os.system("start chrome https://www.facebook.com")  
    elif command.startswith("play music"): 
        song_name = command.lower().replace("play music", "").strip()# Extract the song name from the command
        if song_name in musiclib.music:
            os.system(f"start chrome {musiclib.music[song_name]}")
        else:
            speak("Sorry, I couldn't find that song in the library.")  

    else:
        speak("Sorry, I didn't understand that command.")    

if __name__ == "__main__":# Main function to run the assistant
    speak("initializing jarvis")
    try:# Continuously listen for voice commands
        while True:
            # obtain audio from the microphone
            r = sr.Recognizer()
            print("Listening...")

            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                # recognize speech using Google Speech Recognition
                
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
                process_command(r.recognize_google(audio))

    except Exception as e:
        print("Error: {0}".format(e))
         

