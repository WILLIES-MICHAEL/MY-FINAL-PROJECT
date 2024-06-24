__Owner__ = 'User'
import sqlite3

db = sqlite3.connect('USERS REGISTER.db')
try:
    cursor = db.cursor()

    cursor.execute('''CREATE TABLE register (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    surname VARCHAR(40) NOT NULL,
    other name VARCHAR(20) NOT NULL,
    gender  VARCHAR(10) NOT NULL,
    position VARCHAR(10) NOT NULL,
    username VARCHAR(20) NOT NULL,
    password VARCHAR(50) NOT NULL);''')
    db.commit()

    cursor.execute('''CREATE TABLE Compose (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    from VARCHAR(40) NOT NULL,
    subject name VARCHAR(20) NOT NULL,
    to  VARCHAR(10) NOT NULL,
    message VARCHAR(10) NOT NULL;''')
    db.commit()

    print('table(s) created successfully')

except:
    print('error in operation')
    #db.rollback()
db.close()