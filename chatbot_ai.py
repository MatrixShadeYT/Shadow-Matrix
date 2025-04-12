

def message(text):
    return "Response."

conversation = {
    "user": [],
    "bot": []
}

def response(text):
    output = message(text)
    conversation['user'].append(text)
    conversation['bot'].append(output)
    return output