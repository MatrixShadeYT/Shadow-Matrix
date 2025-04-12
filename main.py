from speech_to_text import microphone
from text_to_speech import speech
import chatbot_ai

speech('Program started')
print('BOT: Program started.')

while True:
    mic = microphone()
    if mic == "Exit program.":
        print('Shade: Exit program.')
        speech('Exiting program.')
        print('BOT: Exiting program.')
        break
    response = chatbot_ai.response(mic,'Shade')
    speech(response.replace('\n',' '))
    print("BOT: {0}".format(response))
database.close()