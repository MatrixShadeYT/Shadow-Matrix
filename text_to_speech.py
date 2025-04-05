import pyttsx3
engine = pyttsx3.init()
def speech(text):
    if ("0+f1" in text.lower().replace(' ','')):
        engine.setProperty('voice', engine.getProperty('voices')[0].id+'+f1')
        print('tone: 0+f1')
    if ("boy" in text.lower()):
        engine.setProperty('voice', engine.getProperty('voices')[0].id)
        print('tone: 0')
    if ("girl" in text.lower()):
        engine.setProperty('voice', engine.getProperty('voices')[1].id)
        print('tone: 1')
    engine.say(text)
    engine.runAndWait()