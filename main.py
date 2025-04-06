from speech_to_text import microphone
from text_to_speech import speech
#import pyaudio
import time
print('Program started.')
speech('Program started.')
while(True):
    mic = microphone()
    if (mic == "stop"):
        print('System: COMMAND STOP DETECTED!\nExiting program.')
        speech('Exiting program.')
        break
    response = "Response."
    print("ME: {0}".format(mic))
    print("BOT: {0}".format(response))
    speech(response)