import sqlite3
import os

connection = sqlite3.connect('ShadowAI.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS dataset (
    id TEXT PRIMARY KEY,
    response_id TEXT UNIQUE,
    input text,
    output text
)''')
connection.commit()

def getPrevious(inputed):
    cursor.execute("SELECT * FROM dataset WHERE input = :input",{'input':inputed})
    return cursor.fetchall()

def getList():
    cursor.execute("SELECT * FROM dataset")
    return cursor.fetchall()

def enter(inputed, outputed):
    with connection:
        cursor.execute(
            "INSERT INTO dataset VALUES (:input, :output)",
            {'input': inputed, 'output': outputed}
        )

def removeItem(inputed,outputed):
    with connection:
        cursor.execute(
            "DELETE from dataset WHERE input = :input AND output = :output",
            {'input': inputed,'output': outputed}
        )

def close():
    connection.close()