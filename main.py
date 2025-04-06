from speech_to_text import microphone
from text_to_speech import speech
#import pyaudio
print("Program Began")
while(True):
    speech('Ready.')
    mic = microphone()
    speech('Processing.')
    if (mic == "stop"):
        speech('Exiting program.')
        break
    print("ME: {0}".format(mic))
print("Program Over")