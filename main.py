from speech_to_text import microphone
from text_to_speech import speech
#import pyaudio
import time
print('Program started.')
speech('Program started.')
while(True):
    mic = microphone()
    if (mic == "stop"):
        print('Exiting program.')
        speech('Exiting program.')
        break
    print("ME: {0}".format(mic))