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

cursor.execute("""DROP TABLE SavedCode""")

sql_command = """
CREATE TABLE SavedCode (
code LONGTEXT()
)
"""

cursor.execute(sql_command)

conn.commit()

conn.close()
