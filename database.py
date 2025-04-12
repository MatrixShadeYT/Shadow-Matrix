import sqlite3
import os

connection = sqlite3.connect('ShadowAI.db')
cursor = connection.cursor()

def create_table(table):
    with connection:
        cursor.execute('''CREATE TABLE IF NOT EXISTS :table (
            input text,
            output text
        )''', {'table': table})

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