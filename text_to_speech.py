import pyttsx3
.
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[1].id)

def speech(text,file=False):
    if file == True:
        engine.save_to_file(text,'output')
    else:
        engine.say(text)
    engine.runAndWait()