#Zach Boyle 2018
import socket     
import time 
import _thread
from chat import *
message_chain=[]
#test threading/receiving code
s = socket.socket() 
host = socket.gethostname() 
port = 12345     
s.connect((host, port))
global board_label 
def receiver(named,timed): 
   while True:
      print("ready to go")
      receiver.rea=s.recv(1024).decode()
      print(receiver.rea)
      board_update(receiver.rea)
def sender(messi): 
   message2=messi
   s.send(message2.encode())  
def runner():
   _thread.start_new_thread(receiver,("Thread-1", 0.1, ))
runner()

    
          