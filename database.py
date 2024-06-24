import sqlite3

c = sqlite3.connect('email.db')
try:
    cursor = c.cursor()

    ### REGISTRATION TABLE
    my_registration_table = '''create table register(staffid integer primary key autoincrement, surname varchar(30), firstname varchar(30), gender varchar(6), email varchar(30), state varchar(30), position varchar(25));'''
    cursor.execute( my_registration_table )

    ### LOGIN TABLE
    loginsql = '''create table login(id integer primary key autoincrement, username varchar(50) not null, password varchar(50) not null);'''
    cursor.execute(loginsql)

   ### MESSAGE TABLE
    my_message_table = '''create table message(id integer primary key autoincrement, sender varchar(30), receiver varchar(30), subject varchar(30), message varchar(500), messagedate varchar(10))'''

    cursor.execute( my_message_table )

    c.commit()

    print('table(s) created successfully')
except:
    print('error in table creation')
c.close()


