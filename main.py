from speech_to_text import microphone
from text_to_speech import speech
#import pyaudio
print("Program Began")
while(True):
    speech('Ready to listen for speech.')
    mic = microphone()
    speech('Processing, One moment.')
    if (mic == "stop"):
        break
    print("ME: {0}".format(mic))
print("Program Over")