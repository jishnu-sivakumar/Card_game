import socket               # Import socket module
import time
import threading
import pickle
from prototype_ import Players, Cards


s = 0
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

   name_dict = {}

   def __init__(self):
      global s
      s.listen()
      i = 0
      p = {}
      self.o = 0

      self.player_no = 0
      v = len(self.name_dict)
      while True:
         #print("len:  ", v)
         if v == 8:
            break

         elif  v >=4:
            self.c, self.addr = s.accept()
            print("main")
            self.card_decider()
            v+= 1
         elif v< 4:
            self.c, self.addr = s.accept()
            print("init")
            p["Main_thread" + str(i)] = threading.Thread(target=self.e, args=())
            p["Main_thread" + str(i)].start()
            v+= 1
            i += 1


   def snd(self,data):
      message = data.encode(self.FORMAT)
      self.c.send(message)
      print("sending...:", data)


   def e(self):
      byte_dic = pickle.dumps(self.name_dict)
      self.c.send(byte_dic)

      byte_dic = self.c.recv(4092)
      dat = pickle.loads(byte_dic)
      self.name_dict = dat
      print(self.name_dict)

   def card_decider(self):
      if self.o == 0:
         Cards.Shuffle(self.name_dict)
         self.o +=1
      name = self.c.recv(1024).decode()
      for i in self.name_dict:
         #print("i is",self.name_dict[i])
         if name == i:
            #print(self.name_dict[i])
            dato = pickle.dumps(self.name_dict[i])
            self.c.send(dato)




spam()



