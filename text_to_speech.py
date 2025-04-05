import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice', voices[1].id)
def speech(text):
    engine.say(text)
    engine.runAndWait()