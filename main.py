from speech_to_text import microphone
from text_to_speech import speech
#import pyaudio
import time
speech('Program started.')
print('Program started.')
while(True):
    mic = microphone()
    if (mic == "stop"):
        print('System: COMMAND STOP DETECTED!')
        speech('Exiting program.')
        print('Exiting program.')
        break
    response = "Response."
    print("ME: {0}".format(mic))
    speech(response)
    print("BOT: {0}".format(response))