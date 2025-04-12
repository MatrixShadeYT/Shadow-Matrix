from speech_to_text import microphone
from text_to_speech import speech
import chatbot_ai

speech('Program started')
print('BOT: Program started.')

while True:
    mic = microphone().lower()
    if mic == "exit program":
        speech('Exiting program.')
        print('BOT: Exiting program.')
        break
    response = chatbot_ai.response(mic)
    track = False
    for i in ['who','what','where','why','when','how']:
        if i in mic:
            question = True
    if question == True:
        print("ME: {0}".format(mic[0].upper()+mic[1:]+"?"))
        question = False
    else:
        print("ME: {0}".format(mic[0].upper()+mic[1:]+"."))
        speech(response.replace('\n',' '))
    print("BOT: {0}".format(response))