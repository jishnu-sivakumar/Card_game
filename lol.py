import socket
import pickle

class Main:

    def __init__(self):
        self.s = socket.socket()
        host = socket.gethostname()
        IPaddr = '26.4.87.63'
        port = 60070
        self.s.connect((IPaddr, port))
        while True:

            print(self.s.send(input("wnter: ").encode()))


Main()