import pyttsx3
engine = pyttsx3.init()
def speech(text):
    if (text.lower().replace(' ','') == "0+f1"):
        engine.setProperty('voice', engine.getProperty('voices')[0].id+'+f1')
        print('tone: 0+f1')
    if (text.lower() == "boy"):
        engine.setProperty('voice', engine.getProperty('voices')[0].id)
        print('tone: 0')
    if (text.lower() == "girl"):
        engine.setProperty('voice', engine.getProperty('voices')[1].id)
        print('tone: 1')
    engine.say(text)
    engine.runAndWait()