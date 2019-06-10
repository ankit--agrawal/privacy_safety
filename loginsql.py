import sqlite3
#implement password check
def log_in(user,passw):
   conn= sqlite3.connect('useraccount.db')
   cursor = conn.execute("SELECT * from USERACC WHERE ID=(?) AND PASS=(?)",(user,passw)) 
   is_true=False
   for row in cursor:
      if row[0]==user and row[1]==passw:
         print(row)
         is_true=True
   if is_true!=True:
      print("WTF")
      
   
   