#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import time
import _thread
import threading 
from _thread import *
send_count=0
clients=[]
addresses=[]
messageq=[]
def on_new_client(clientsocket,addr):
   while True:
      print("new client")
      message=clientsocket.recv(1024)
      print(message.decode())
      messageq.append(message.decode()+"\n")
      send_mess(clientsocket,addr)
def send_mess(clien,addre):
   global send_count
   #for cl in clients:
      #for ad in addresses:
   for mes in messageq:
      clien.send(mes.encode())
      send_count=send_count+1
      #pop_mess(send_count)
            
def pop_mess(count):
   if count>1:
      messageq.pop(0)
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)


                  # Now wait for client connection.
while True:    # Establish connection with client. 
   c, addr = s.accept()
   clients.append(c)
   addresses.append(addr)
   #_thread.start_new_thread(on_new_client,(cl,ad))
   for cl in clients:
      for ad in addresses:
         threading.Thread(target=on_new_client, args=(cl,ad)).start()