import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO clients (nom, prenom, messages) VALUES (?, ?, ?)",('DUPONT', 'Emilie', 'Je veux te recruter'))



connection.commit()
connection.close()
