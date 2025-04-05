from speech_to_text import microphone
from text_to_speech import speech
#import pyaudio
print("Program Began")
while(True):
    mic = microphone()
    if (mic == "stop"):
        break
    print("ME: {0}".format(mic))
    speech(mic)
print("Program Over")