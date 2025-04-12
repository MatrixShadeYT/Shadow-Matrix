import speech_recognition as sr

r = sr.Recognizer()

def formatText(text):
    text = text.lower()
    question = False
    for i in ['who','what','where','why','when','how']:
        if i in text:
            question = True
    if question == True:
        return '{0}'.format(text[0].upper()+text[1:]+"?")
    else:
        return '{0}'.format(text[0].upper()+text[1:]+".")

def microphone():
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source,duration=0.1)
                audio = r.listen(source)
                MyText = r.recognize_google(audio)
                text = format(MyText)
                return text
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occurred.")