# Creation of Shadow AI
I started this project because I saw Neuro-san from videl's channel and thought it might be a fun project to work on making myself one. It's definitely a lot more complex than I expected. There's tons of levels for what you need to do.
Here's a list of what you need to make in order to create a chatbot.
1 Speech-to-text, 2 Database, 3 Chatbot, 4 Text-to-speech<br>
But... Wait... If I'm going for something like Neuro-sama then I'll need to make a character model, animate in live2d then make it work with vtube studio.
5 Create-Model, 6 Animate, 7 Vtube-studio, 8 Movement.
## Speech-To-Text
For my speech to text I used "speech_recognition". It's a default import so you don't have to worry about installing it. You can use lots of different ones but this is the one I went with.<br>
```python
import speech_recognition as sr
r = sr.Recognizer()
def microphone():
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.1)
                audio = r.listen(source)
                MyText = r.recognize_google(audio)
                return MyText
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occurred.")
```

## Database
I went with "sqlite3" which is another default import. There are lots of options out there, I just found this one the easiest to deal with.<br>
```python
import sqlite3
connection = sqlite3.connect(':memory:')
cursor = connection.cursor()
with connection:
    cursor.execute('''CREATE TABLE IF NOT EXISTS dataset (
        user TEXT,
        input TEXT,
        output TEXT
    )''')
with connection:
    cursor.execute(
        "INSERT INTO dataset VALUES (:user, :input, :output)",
        {'user': 'USERNAME', 'input': 'Hi.', 'output': 'Hello.'}
    )
cursor.execute("SELECT * FROM dataset")
print(cursor.fetchall())
with connection:
    cursor.execute(
        "DELETE FROM dataset WHERE user = :user AND input = :input AND output = :output",
        {'user': 'USERNAME', 'input': 'Hi.', 'output': 'Hello.'}
    )
cursor.execute("SELECT * FROM dataset")
print(cursor.fetchall())
connection.close()
```

## Chatbot
TEXT
```python
import keras
inputed = ["Hi!","How are you?"]
expect = ["Hello.","Good."]
model = keras.Sequential([
    keras.Input(shape=(180,)),
    keras.layers.Dense(32, activation="relu"),
    keras.layers.Dense(10, activation="sigmoid")
])
model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['accuracy']
)
model.fit(
    inputed,
    expect,
    epochs=100
)
```

## Text-To-Speech
This is just a prototype for now.
```python
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice',engine.getProperty('voices')[1].id)
def speech(text,file=False):
    if file == True:
        engine.save_to_file(text,'output')
    else:
        engine.say(text)
    engine.runAndWait()
```

## Create-Model
TEXT

## Animate
TEXT

## Vtube-Studio
TEXT

## Movement
TEXT