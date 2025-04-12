import database

data = database()

def message(text,user):
    output = "Bot." if text & user else "Human."
    return output

def response(text,user):
    output = message(text,user)
    database.enter(user,text,output)
    return output