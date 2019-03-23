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
    cursor.execute("""SELECT MAX(codeID) FROM savedCode""")
    max_id = cursor.fetchone()[0]

    print(max_id)
    cursor.execute("SELECT codeID FROM savedCode WHERE codeID = (?)", (max_id,))
    identification = cursor.fetchone()[0]
    cursor.execute("SELECT timeStamp FROM savedCode WHERE codeID = (?)", (max_id,))
    time_stamp = cursor.fetchone()[0]

    out += "Successfully Submitted to database: \n"
    out += "\tID = {}\n".format(identification)
    out += "\tTimeStamp = {}\n".format(str(time_stamp))
    conn.commit()
    print(out)


def get_code(code_id):
    cursor.execute("SELECT code FROM savedCode WHERE codeID = (?)", (code_id,))
    return cursor.fetchone()[0]


conn.commit()

#conn.close()
