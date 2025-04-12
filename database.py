import sqlite3
import os

connection = sqlite3.connect('ShadowAI.db')
cursor = connection.cursor()

# Dataset
with connection:
    cursor.execute('''CREATE TABLE IF NOT EXISTS dataset (
        input TEXT,
        output TEXT
    )''')

# Training data
with connection:
    cursor.execute('''CREATE TABLE IF NOT EXISTS training (
        input TEXT,
        output TEXT
    )''')

def getPrevious(inputed,table):
    cursor.execute("SELECT * FROM :table WHERE input = :input",{'table': table,'input':inputed})
    return cursor.fetchall()

def getList(table):
    cursor.execute("SELECT * FROM :table", {'table': table})
    return cursor.fetchall()

def enter(inputed, outputed, table):
    with connection:
        cursor.execute(
            "INSERT INTO :table VALUES (:input, :output)",
            {'table': table,'input': inputed, 'output': outputed}
        )

def removeItem(inputed,outputed):
    with connection:
        cursor.execute(
            "DELETE FROM :table WHERE input = :input AND output = :output",
            {'table': table,'input': inputed,'output': outputed}
        )

def close():
    connection.close()