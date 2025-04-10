from speech_to_text import microphone
from text_to_speech import speech
import chatbot_ai

speech(input("Text: "))

#speech('Program started')
#print('BOT: Program started.')

while 1 == 0:
    mic = microphone().lower()
    if mic == "exit program":
        speech('Exiting program.')
        print('BOT: Exiting program.')
        break
    response = chatbot_ai.response(mic)
    track = False
    if 'who' in mic:
        print("ME: {0}".format(mic[0].upper()+mic[1:]+"?"))
    elif 'what' in mic:
        print("ME: {0}".format(mic[0].upper()+mic[1:]+"?"))
    elif 'where' in mic:
        print("ME: {0}".format(mic[0].upper()+mic[1:]+"?"))
    elif 'why' in mic:
        print("ME: {0}".format(mic[0].upper()+mic[1:]+"?"))
    elif 'when' in mic:
        print("ME: {0}".format(mic[0].upper()+mic[1:]+"?"))
    elif 'how' in mic:
        print("ME: {0}".format(mic[0].upper()+mic[1:]+"?"))
    else:
        print("ME: {0}".format(mic[0].upper()+mic[1:]+"."))
    speech(response.replace('\n',' '))
    print("BOT: {0}".format(response))