import sqlite3

db = sqlite3.connect('WILLIES DB.db')
try:
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE staffinfo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    studentname VARCHAR(40) NOT NULL,
    birthdate VARCHAR(10) NOT NULL,
    department VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL);''')
    db.commit()
    print('table(s) created successfully')
except:
    print('error in table creation')
db.close()