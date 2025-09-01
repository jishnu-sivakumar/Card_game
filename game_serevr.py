import socket
import time
import threading
import pickle




class spam:

   i = 0
   FORMAT = 'utf-8'
   HEADER = 64
   s = socket.socket()         # Create a socket object
   host = socket.gethostname()# Get local machine name
   IPaddr = socket.gethostbyname(host)
   print(IPaddr)
   port = 60071            # Reserve a port for your service.
   s.bind((IPaddr, port))        # Bind to the port

   def __init__(self):

      global lis
      global trump_decided
      global client_sockets
      client_sockets = []
      self.s.listen(4)
      lis = []
      trump_decided = False
      i = 0
      while True:
         self.c, self.addr = self.s.accept()
         self.e()
         t = threading.Thread(target= self.Round_main, args= (self.c,)).start()





   def snd(self,data):
      message = data.encode(self.FORMAT)
      self.c.send(message)
      print("sending...:", data)


   def e(self):
      global lis
      self.c.send(pickle.dumps(lis))
      lis= pickle.loads(self.c.recv(2048))

      print(self.c,"connectedd", lis[-1])

   def Round_main(self, cli):
      i = 0
      trump_revealed = False
      global client_sockets
      client_sockets.append(cli)

      a = 0
      self.rev = False
      self.lop = []
      while True:
         global lis
         global trump_decided

         if len(lis)>= 4:

            print(cli,"its" ,lis[i] +"'s turn" "ROUNFDD", i)

            t = cli.recv(2049)
            dec = pickle.loads(t)
            print(dec)
            if "roundover" in dec.values():
               if i == 3:
                  i = 0

               else:
                  i += 1

            elif lis[i] in dec.keys():
               print("yes")

               if trump_decided == False:
                  cli.send("trump?".encode())
                  trump_card = pickle.loads(cli.recv(2049))
                  trump_decided = True
                  print("trump card is", trump_card)
                  time.sleep(0.1)
                  for e in trump_card:
                     oj = [trump_card[e], 1]
                     print(oj)
                     self.broadcastd(pickle.dumps(oj))


               elif trump_decided == True:
                  cli.send("yes".encode())
                  while True:
                     current_card = pickle.loads(cli.recv(2049))
                     if "ask trump?" in current_card.values():
                        if a == 0:
                           self.broadcast("trump reveal!!".encode(), cli)
                           a = 69

                     elif "cani ?" not in current_card.values():
                        self.broadcast(pickle.dumps(current_card), cli)
                        for i in current_card:
                           self.lop.append(current_card)
                        break



            elif lis[i] not in dec.keys():
               print("not your turn")
               cli.send("no".encode())

            if len(self.lop) == 4:
               ma = 0
               dei = None

               for y in self.lop:
                  for u in y:
                     print("yu is ", y[u].worth)
                     if y[u].worth > ma:
                        ma = y[u].worth
                        print(ma)
                        dei = u
               print(dei, "is winner")
               self.winner = str(dei)
               self.broadcast(pickle.dumps({"winner":self.winner}), cli)
               self.lop = []
            time.sleep(0.1)
            print("=====================")

   def broadcastd(self, message):
      for client_socket in client_sockets:
         client_socket.send(message)

   def broadcast(self,message, cli):
      global client_sockets
      for client_socket in client_sockets:
            client_socket.send(message)


   def Round_ser(self):
      print("in round server")
      name = self.c.recv(4092).decode()

      print(name)
      l = [0,0,0,0]
      p = 0
      di = self.name_dict
      round = 0
      while True:
         for i in di:
            di[i] = 0
         for i in di:
            try:
               di[old_i] = 0
            except:
               pass

            di[i] = 1
            print(round)
            print(di)
            p += 1
            old_i = i
            jj = pickle.dumps(di)
            self.c.sendto(jj, self.addr)
            if round == 0:
               dd = self.c.recv(2049)
               trump_card = pickle.loads(dd)
               print("trump card is: ", trump_card)

            if round >=1:

               lol = self.c.recv(2045)
               recievend_card = pickle.loads(lol)
               print(recievend_card)
               p = self.c.sendto(lol, self.addr)

            round += 1


spam()