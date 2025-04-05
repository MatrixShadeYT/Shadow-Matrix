import pyttsx3
engine = pyttsx3.init()
def speech(text):
    if (text.lower().replace(' ','') == "0+f1"):
        engine.setProperty('voice', engine.getProperty('voices')[0].id+'+f1')
    elif (text.lower().replace('plus ','+') == "0+f2"):
        engine.setProperty('voice', engine.getProperty('voices')[0].id+'+f2')
    elif (text.lower().replace('plus ','+') == "0+f3"):
        engine.setProperty('voice', engine.getProperty('voices')[0].id+'+f3')
    elif (text.lower().replace('plus ','+') == "0+f4"):
        engine.setProperty('voice', engine.getProperty('voices')[0].id+'+f4')
    elif (text.lower().replace('plus ','+') == "1+f4"):
        engine.setProperty('voice', engine.getProperty('voices')[1].id+'+f1')
    elif (text.lower().replace('plus ','+') == "1+f2"):
        engine.setProperty('voice', engine.getProperty('voices')[1].id+'+f2')
    elif (text.lower().replace('plus ','+') == "1+f3"):
        engine.setProperty('voice', engine.getProperty('voices')[1].id+'+f3')
    elif (text.lower().replace('plus ','+') == "1+f4"):
        engine.setProperty('voice', engine.getProperty('voices')[1].id+'+f4')

    engine.say(text)
    engine.runAndWait()