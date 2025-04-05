from speech_to_text import microphone
print("Program Began")
while(True):
    mic = microphone()
    if (mic == "stop"):
        break
    print("ME: {0}".format(mic))
print("Program Over")