# Code passes the PEP8 Check.
import sqlite3

conn = sqlite3.connect('assignment.db')

try:
    conn = sqlite3.connect("assignment.db")
except Exception as e:
    print(e)
else:
    print("Finishing connecting to database")

cursor = conn.cursor()

#cursor.execute("""DROP TABLE IF EXISTS savedCode""")


def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS savedCode(
    codeID INTEGER PRIMARY KEY AUTOINCREMENT,
    timeStamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    code LONGTEXT)""")


def data_entry(code):
    out = ''

    cursor.execute("""INSERT INTO savedCode (code) values(?)""", (code,))
    max_id = cursor.execute("""SELECT MAX(codeID) FROM savedCode""")
   # """SELECT id FROM tickets WHERE "Status" = 'Pending'"""
    print(max_id)
    #identification = cursor.execute("SELECT codeID FROM savedCode WHERE codeID = (?)", (max_id,))
    #time_stamp = cursor.execute("SELECT timeStamp FROM savedCode WHERE codeID = (?)", (max_id,))
    identification = cursor.execute("SELECT codeID FROM savedCode WHERE codeID = 1")
    time_stamp = cursor.execute("SELECT timeStamp FROM savedCode WHERE codeID = 1")
    out += "Successfully Submitted to database: \n"
    out += "\tID = {}\n".format(identification)
    out += "\tTimeStamp = {}\n".format(str(time_stamp))
    conn.commit()
    print(out)


def get_code():
    return cursor.execute("SELECT code FROM savedCode WHERE codeID = 1")


conn.commit()

#conn.close()
