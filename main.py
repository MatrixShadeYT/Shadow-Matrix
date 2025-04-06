from speech_to_text import microphone
from text_to_speech import speech
import chatbot_ai
#import pyaudio
import time
print('Program started.')
while True:
    mic = microphone()
    if mic.lower() == "exit program":
        print('Exiting program.')
        break
    response = chatbot_ai.response(mic)
    track = False
    for i in ["who","what","where","why","when","how"]:
        if track == False:
            if i in mic:
                print("ME: {0}".format(mic[0].upper()+mic[1:]+"?"))
                track = True
            else:
                print("ME: {0}".format(mic[0].upper()+mic[1:]+"."))
                track = True
    speech(response.replace('\n',' '))
    print("BOT: {0}".format(response))