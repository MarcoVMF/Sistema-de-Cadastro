import sqlite3
import datetime
import os

con = sqlite3.connect('database.db')


cur = con.cursor()

cur.execute("CREATE TABLE user(id INTEGER PRIMARY KEY, username TEXT, name TEXT, password TEXT, email TEXT, createdDate DATE, updatedDate DATE)")

