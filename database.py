from random import randint
import sqlite3
import os

# Initiate the connection
connection = sqlite3.connect('ShadowAI.db')
cursor = connection.cursor()

with connection:
    cursor.execute('''CREATE TABLE IF NOT EXISTS dataset (
        user TEXT,
        input TEXT,
        output TEXT
    )''')

# Get values by user
def getByUser(user):
    cursor.execute("SELECT * FROM dataset WHERE user = :user",{'user':user})
    return cursor.fetchall()

# Get values by input
def getByInput(inputed):
    cursor.execute("SELECT * FROM dataset WHERE input = :input",{'input':inputed})
    return cursor.fetchall()

# Get values by output
def getByOutput(outputed):
    cursor.execute("SELECT * FROM dataset WHERE output = :output",{'output':outputed})
    return cursor.fetchall()

# Get list of database
def getList():
    cursor.execute("SELECT * FROM dataset")
    return cursor.fetchall()

# Add values to database
def enter(user,inputed,outputed):
    with connection:
        cursor.execute(
            "INSERT INTO dataset VALUES (:user, :input, :output)",
            {'user': user,'input': inputed, 'output': outputed}
        )

# Remove item from Database
def removeItem(user,inputed,outputed):
    with connection:
        cursor.execute(
            "DELETE FROM dataset WHERE user = :user AND input = :input AND output = :output",
            {'user': user,'input': inputed,'output': outputed}
        )

def clearItems():
    listed = getList()
    for i in listed:
        removeItem(i[0],i[1],i[2])

# Close the connection to database
def close():
    connection.close()