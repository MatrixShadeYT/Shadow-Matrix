import sqlite3

connection = sqlite3.connect('ShadowAI.db')
cursor = connection.cursor()

c.execute('''CREATE TABLE dataset (
          input text,
          output text,
)''')