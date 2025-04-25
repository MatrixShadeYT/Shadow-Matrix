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
model.fit(x_train,y_train,epochs=10)

def request(text,user):
    output = ""
    return output

def response(text,user):
    output = request(text,user)
    database.enter(user,text,output)
    return output