import neural_network
import database
import string

tokenizer = list(' ,.!?*:'+string.ascii_lowercase)
formatting = [
    ['and','&'],
    ['dollar','$'],
    ['percent','%'],
    ['hashtag','#']
]
data = database.dataset()
model = neural_network.model([
    neural_network.layer(32),
    neural_network.layer(10)
])

def textTokenizer(text):
    x = ''
    for i in text:
        x = f'{x}{tokenizer.index(i)}'
    for i in formatting:
        x.replace(i[0],i[1])
    return x

def textualize(text):
    x = ''
    for i in text:
        x = f'{x}{tokenizer[i]}'
    return x

def request(text,user):
    text = textTokenizer(f'{user}:{text}')
    output = model.predict(text,batch_size=1,verbose=0)
    return textualize(output)

def response(text,user):
    output = request(text,user)
    database.enter(user,text,output)
    return output