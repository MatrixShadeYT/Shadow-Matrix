from speech_to_text import microphone
from text_to_speech import speech
#import pyaudio
import time
time.sleep(1)
speech('Program started.')
print('Program started.')
while(True):
    mic = microphone()
    if (mic == "stop"):
        break
    print("ME: {0}".format(mic))
time.sleep(1)
speech('Exiting program.')
print('Exiting program.')