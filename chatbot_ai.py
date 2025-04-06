conversation = {
    "user": [],
    "bot": []
}

def message(text):
    return "Response."

def response(text):
    if text == "end conversation":
        conversation['user'] = []
        conversation['bot'] = []
        return "Clearing Records.\n\n"
    else:
        output = message(text)
        conversation['user'].append(text)
        conversation['bot'].append(output)
        return output