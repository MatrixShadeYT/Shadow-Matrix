from speech_to_text import mic_process
print("Program Began")
while(True):
    mic = mic_process()
    if (mic == "stop"):
        break
    print("ME: {0}".format(mic))
print("Program Over")