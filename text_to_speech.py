import pyttsx3
engine = pyttsx3.init()
def speech(text):
    if (text.lower().replace(' ','') == "0+f1"):
        engine.setProperty('voice', engine.getProperty('voices')[0].id+'+f1')
        print('tone: 0, +f1')
    if (text.lower().replace('plus ','+') == "0+f2"):
        engine.setProperty('voice', engine.getProperty('voices')[0].id+'+f2')
        print('tone: 0, +f2')
    if (text.lower().replace('plus ','+') == "0+f3"):
        engine.setProperty('voice', engine.getProperty('voices')[0].id+'+f3')
        print('tone: 0, +f3')
    if (text.lower().replace('plus ','+') == "0+f4"):
        engine.setProperty('voice', engine.getProperty('voices')[0].id+'+f4')
        print('tone: 0, +f4')
    if (text.lower().replace('plus ','+') == "1+f4"):
        engine.setProperty('voice', engine.getProperty('voices')[1].id+'+f1')
        print('tone: 1, +f1')
    if (text.lower().replace('plus ','+') == "1+f2"):
        engine.setProperty('voice', engine.getProperty('voices')[1].id+'+f2')
        print('tone: 1, +f2')
    if (text.lower().replace('plus ','+') == "1+f3"):
        engine.setProperty('voice', engine.getProperty('voices')[1].id+'+f3')
        print('tone: 1, +f3')
    if (text.lower().replace('plus ','+') == "1+f4"):
        engine.setProperty('voice', engine.getProperty('voices')[1].id+'+f4')
        print('tone: 1, +f4')
    engine.say(text)
    engine.runAndWait()