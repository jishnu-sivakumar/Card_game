import socket
import pickle

class Round_Client:
    def __init__(self):
        self.s = socket.socket()
        host = socket.gethostname()

        IPaddr = '26.4.87.63'
        port = 60070
        self.s.connect((IPaddr, port))


    def round_client(self):
        dat = [0,0,1,0]
        ee = pickle.dumps(dat)
        self.s.send(ee)