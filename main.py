from speech_to_text import microphone
import bot
print("Program Began")
while(True):
    mic = microphone()
    if (mic == "stop"):
        break
    print("ME: {0}".format(mic))
    response = bot.response(mic)
    print("Bot: {0}".format(response))
print("Program Over")