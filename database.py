import sqlite3
import os

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE conversation (
    input text,
    output text
)''')
connection.commit()

def previous():
    pass

def input():
    pass

def close():
    connection.close()