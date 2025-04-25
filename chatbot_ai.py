import database
import string
import keras

tokenizer = list(' ,.!?*:'+string.ascii_lowercase)
formatting = [
    ['and','&'],
    ['dollar','$'],
    ['percent','%'],
    ['hashtag','#']
]
data = database.dataset()
model = keras.Sequential([
    keras.Input(shape=(180)),
    keras.layers.Dense(32, activation="relu"),
    keras.layers.Dense(10, activation="sigmoid")
])
model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['accuracy']
)
model.fit(
    [ # NAME:Input
        f"{i[0]}:{i[1]}" for i in data.getList()
    ],
    [ # Output
        f"{i[2]}" for i in data.getList()
    ],
    epochs=100
)

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