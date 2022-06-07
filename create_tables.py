import sqlite3

conn = sqlite3.connect('Staff.db')
c = conn.cursor()

c.execute("""CREATE TABLE Staff(
    Staff_ID INTEGER PRIMARY KEY,
    First_Name TEXT,
    Last_Name TEXT,
    Area TEXT
)""")

c.execute("""CREATE TABLE Areas(
    Area_Name TEXT,
    Staff_ID INTEGER,
    FOREIGN KEY(Staff_ID) REFERENCES Staff(Staff_ID)
)""")

conn.commit()
conn.close()