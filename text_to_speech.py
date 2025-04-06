import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[0].id)
def speech(text):
    engine.say(text)
    engine.runAndWait()