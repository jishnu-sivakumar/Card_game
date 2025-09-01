import socket
import pickle
import threading

class spam:
   global s
   i = 0
   FORMAT = 'utf-8'
   HEADER = 64
   s = socket.socket()         # Create a socket object
   host = socket.gethostname()# Get local machine name
   IPaddr = socket.gethostbyname(host)
   print(IPaddr)
   port = 60070                # Reserve a port for your service.
   s.bind((IPaddr, port))        # Bind to the port



   def __init__(self):
      global s
      s.listen()
      self.l = []
      while True:
          self.c, self.addr = s.accept()
          print("connected")
          self.l.append(self.addr)
          t = threading.Thread(target= self.e).start()
   def e(self):
       while True:
           t =  self.c.recv(2048).decode()
           if "yes" in t:
               print("it was a yes")

           if "no" in t:
               print("it was  a no")





spam()