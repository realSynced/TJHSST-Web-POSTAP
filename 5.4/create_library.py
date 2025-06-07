import sqlite3

connection = sqlite3.connect("database.db")

with open("library_information.sql") as f:
    connection.executescript(f.read())
