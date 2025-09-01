import socket
import time
import pickle

class Main:

    def __init__(self):
        self.s = socket.socket()
        host = socket.gethostname
        IPaddr = '26.4.87.63'
        port = 60070
        self.s.connect((IPaddr, port))
        dicb = self.s.recv(2049)
        dic = pickle.loads(dicb)
        print(dic)

        self.s.connect((IPaddr, 60071))
        self.s.send(dicb)