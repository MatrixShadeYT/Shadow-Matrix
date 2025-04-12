import database

data = database()

def message(text,user):
    output = "RESPONSE TO {0} WHO SAID {1}".format(user,text)
    return output

def response(text,user):
    output = message(text,user)
    database.enter(user,text,output)
    return output