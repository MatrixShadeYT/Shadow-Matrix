conversation = {
    "user": [],
    "bot": []
}

def message(text):
    return "Response."

def response(text):
    if text == "End conversation.":
        return "\n\n"
    else:
        output = message(text)
        conversation['user'].append(text)
        conversation['bot'].append(output)
        return output