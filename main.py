from speech_to_text import microphone
from text_to_speech import speech
import chatbot_ai

speech('Program started')
print('System: Program started.')

while True:
    mic = microphone()
    print(f'Shade: {mic}')
    if mic == "exit program":
        speech('Exiting program.')
        print('System: Exiting program.')
        break
    response = chatbot_ai.response(mic,'Shade')
    speech(response.replace('\n',' '))
    print("Shadow: {0}".format(response))