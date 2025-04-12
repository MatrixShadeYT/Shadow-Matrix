conversation = {
    "user": [],
    "bot": []
}

def message(text):
    return "Response."

def response(text):
    output = message(text)
    conversation['user'].append(text)
    conversation['bot'].append(output)
    return output