from random import randint
import sqlite3
import os

# Initiate the connection
connection = sqlite3.connect('ShadowAI.db')
cursor = connection.cursor()

# Training Database
class training:
    # Create Table
    def __init__():
        with connection:
            cursor.execute('''CREATE TABLE IF NOT EXISTS training (
                id TEXT,
                input TEXT,
                output TEXT
            )''')

    # Adds from files using - User|Input|Output
    def addTrainingData(file):
        num = len(getTrainingData())
        listed = []
        with f as open(file,'r'):
            num += 1
            for i in f:
                listed.append([num,i.split('|')[0],i.split('|')[1]])
        for i in listed:
            with connection:
                cursor.execute(
                    "INSERT INTO training VALUES (:input, :output)",
                    {'input': inputed, 'output': outputed}
                )

    # Gets the list of data from the database
    def getTrainingData():
        cursor.execute("SELECT * FROM training")
        return cursor.fetchall()

    # Get specified amount of items randomly
    def getTestingData(ammount):
        tList = getTrainingData()
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

# Dataset Database
class dataset:
    # Create Table
    def __init__():
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
    def enter(user, inputed, outputed):
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

# Close the connection to database
def close():
    connection.close()