# Create SQLdatabase and a table

# impoort SQLite3 library
import sqlite3

#create new datebase if datebase doesn't exit already
conn = sqlite3.connect("new.db")

# get a cursor object to execute sql commands
cursor = conn.cursor()

# create a table
cursor.execute(""" CREATE TABLE population
               (city TEXT, state TEXT, population INT)
               """)
# close datebase connection
conn.close()
