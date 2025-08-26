from speech_to_text import microphone
from text_to_speech import speech
import chatbot_ai
import animate

speech('Program started')
print('System: Program started.')

while True:
    mic = microphone()
    print(f'Shade: {mic}')
    if mic == "exit program":
        print('System: Exiting program.')
        speech('Exiting program.')
        break
    outputs = chatbot_ai.response(mic,'Shade')
    response, acts = animate.scrape(outputs)
    print("Shadow: {0}".format(response))
    animate.run(acts)
    speech(response.replace('\n',' '))