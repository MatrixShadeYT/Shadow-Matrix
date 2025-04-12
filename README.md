# Creation of Shadow AI
I started this project because I saw Neuro-san from videl's channel and thought it might be a fun project to work on making myself one. It's definitely a lot more complex than I expected. There's tons of levels for what you need to do.
Here's a list of what you need to make in order to create a chatbot.
1 Speech-to-text, 2 Database, 3 Chatbot, 4 Text-to-speech

## Speech to text
For my speech to text I used "speech_recognition". It's a default import so you don't have to worry about installing it. You can use lots of different ones but this is the one I went with.

'''
import speech_recognition as sr
r = sr.Recognizer()

def microphone():
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.1)
                audio = r.listen(source)
                MyText = r.recognize_google(audio)
                return MyText
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occurred.")
'''

## Database
I went with "sqlite3" which is another default import. There are lots of options out there, I just found this one the easiest to deal with.

'''

'''