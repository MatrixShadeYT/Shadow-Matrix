import database
import keras

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
    epochs=10
)

def request(text,user):
    output = ""
    return output

def response(text,user):
    output = request(text,user)
    database.enter(user,text,output)
    return output