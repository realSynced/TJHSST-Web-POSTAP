import sqlite3

connection = sqlite3.connect("database.db")

with open("reset_db.sql") as f:
    connection.executescript(f.read())
