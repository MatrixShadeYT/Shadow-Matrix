import sqlite3
import os

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE dataset (
    input text,
    output text
)''')
connection.commit()



def close():
    connection.close()