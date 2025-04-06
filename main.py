from speech_to_text import microphone
from text_to_speech import speech
import chatbot_ai
#import pyaudio
import time
print('Program started.')
while(True):
    mic = microphone()
    if (mic == "stop"):
        print('Exiting program.')
        break
    response = chatbot_ai.response(mic)
    print("ME: {0}".format(mic))
    speech(response)
    print("BOT: {0}".format(response))