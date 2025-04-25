import chatbot_ai

while 1 == 0:
    text = input("Shade: ")
    if text == "End program.":
        print("Shadow: Going to sleep.")
        break
    else:
        res = chatbot_ai.response(text,"Shade")
        print("Shadow: {}".format(res))
chatbot_ai.data.close()