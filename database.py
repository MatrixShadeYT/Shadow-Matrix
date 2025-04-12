from random import randint
import sqlite3
import os

connection = sqlite3.connect('ShadowAI.db')
cursor = connection.cursor()

# Dataset
with connection:
    cursor.execute('''CREATE TABLE IF NOT EXISTS dataset (
        user TEXT,
        input TEXT,
        output TEXT
    )''')

# Training data
with connection:
    cursor.execute('''CREATE TABLE IF NOT EXISTS training (
        id TEXT PRIMARY KEY,
        input TEXT,
        output TEXT
    )''')

def addTrainingData(file):
    listed = []
    with f as open(file,'r'):
        for i in f:
            listed.append([i.split('|')[0],i.split('|')[1]])
    for i in listed:
        with connection:
            cursor.execute(
                "INSERT INTO training VALUES (:input, :output)",
                {'input': inputed, 'output': outputed}
            )

def getTrainingData():
    cursor.execute("SELECT * FROM training")
    return cursor.fetchall()

def getTestingData(ammount):
    tList = getTrainingList()
    listed = []
    nList = []
    for i in range(ammount):
        num = randint(0,len(tList))
        while num in nList:
            num = randint(0,len(tList))
        nList.append(num)
    for i in nList:
        listed.append(tList[i])
    return listed

def getByUser(user):
    cursor.execute("SELECT * FROM dataset WHERE user = :user",{'user':user})
    return cursor.fetchall()

def getByInput(inputed):
    cursor.execute("SELECT * FROM dataset WHERE input = :input",{'input':inputed})
    return cursor.fetchall()

def getByOutput(outputed):
    cursor.execute("SELECT * FROM dataset WHERE output = :output",{'output':outputed})
    return cursor.fetchall()

def getList():
    cursor.execute("SELECT * FROM dataset")
    return cursor.fetchall()

def enter(user, inputed, outputed):
    with connection:
        cursor.execute(
            "INSERT INTO dataset VALUES (:user, :input, :output)",
            {'user': user,'input': inputed, 'output': outputed}
        )

def removeItem(inputed,outputed):
    with connection:
        cursor.execute(
            "DELETE FROM dataset WHERE input = :input AND output = :output",
            {'table': table,'input': inputed,'output': outputed}
        )

def close():
    connection.close()