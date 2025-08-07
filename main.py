from speech_to_text import microphone
from text_to_speech import speech
import chatbot_ai

speech('Program started')
print('BOT: Program started.')

def textualize(text):
    if ['who','what','where','why','when','how'] in text.split(' '):
        text = f"{text}?"
    else:
        text = f"{text}."
    return text.capitalize()

while True:
    mic = textualize(microphone())
    if mic == "Exit program.":
        print('Shade: Exit program.')
        speech('Exiting program.')
        print('BOT: Exiting program.')
        break
    print(f'Shade: {mic}')
    response = chatbot_ai.response(mic,'Shade')
    speech(response.replace('\n',' '))
    print("BOT: {0}".format(response))
database.close()