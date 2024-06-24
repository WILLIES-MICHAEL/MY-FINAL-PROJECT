import sqlite3

connection = sqlite3.connect('email.db')

view_record0 = "select * from message;"

cursor = connection.cursor()
cursor.execute( view_record0 )

while True:
    record = cursor.fetchone()

    if record == None:
        break
    print( record )
connection.close()