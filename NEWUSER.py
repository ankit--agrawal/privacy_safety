import sqlite3
from sqlite3 import *
conn=sqlite3.connect('useraccount.db')
#print ("Opened database successfully");

#conn.execute('''CREATE TABLE USERACC
 #         (ID TEXT PRIMARY KEY     NOT NULL,
  #        PASS           TEXT    NOT NULL,
   #       AGE           TEXT    NOT NULL,
    #      SEX           TEXT    NOT NULL,
     #     NAME           TEXT    NOT NULL,	
      #     ZIP           TEXT    NOT NULL);''')
#print ("Table created successfully");
def connx(id,passwor,age,sex,name,zip):
   print(id+passwor+age)
   conn.execute("INSERT INTO USERACC VALUES (?,?,?,?,?,?)",(id, passwor, age,sex,name,zip));#(ID,PASS,AGE,SEX,NAME,ZIP)
   conn.commit()
