import pyttsx3
engine = pyttsx3.init()
def speech(text):
    engine.say(text)
    engine.runAndWait()