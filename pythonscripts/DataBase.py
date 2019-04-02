# Code passes the PEP8 Check.
# Created by Liam Brydon

import sqlite3

conn = sqlite3.connect('assignment.db')

try:
    conn
except Exception as e:
    print(e)
else:
    print("Finishing connecting to database")

cursor = conn.cursor()

# cursor.execute("""DROP TABLE IF EXISTS savedCode""")


def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS savedCode(
    codeID INTEGER PRIMARY KEY AUTOINCREMENT,
    timeStamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    code LONGTEXT)""")


def data_entry(code):
    out = ''

    cursor.execute("""INSERT INTO
     savedCode (code) values(?)""", (code,))
    cursor.execute("""SELECT MAX(codeID) FROM
     savedCode""")
    max_id = cursor.fetchone()[0]

    print(max_id)
    cursor.execute("SELECT codeID FROM "
                   "savedCode WHERE codeID = (?)", (max_id,))
    identification = cursor.fetchone()[0]
    cursor.execute("SELECT timeStamp FROM "
                   "savedCode WHERE codeID = (?)", (max_id,))
    time_stamp = cursor.fetchone()[0]

    out += "Successfully Submitted to database: \n"
    out += "\tID = {}\n".format(identification - 1)
    out += "\tTimeStamp = {}\n".format(str(time_stamp))
    conn.commit()
    print(out)


def get_code(code_id):
    cursor.execute("""SELECT MAX(codeID)
     FROM savedCode""")
    max_id = cursor.fetchone()[0]
    try:
        if int(code_id) >= max_id:
            return False, "ID doesnt exists in table"
        elif int(code_id) <= 0:
            return False, "ID doesnt exists in table"
        else:
            cursor.execute("SELECT code FROM "
                           "savedCode WHERE codeID = (?)", (code_id,))
            return True, cursor.fetchone()[0]
    except ValueError and TypeError:
        print("Please enter an integer")
    except Exception:
        print(":)")


conn.commit()

# conn.close()
