import socket
import pickle
from prototype_ import Players
FORMAT = 'utf-8'
HEADER = 64



s = socket.socket()
host = socket.gethostname()


def snd(data):
    message = data.encode(FORMAT)
    s.send(message)
    #print("sending...:", data)

class main:
    def __init__(self, player):
        IPaddr = '127.0.0.1'
        port = 5005
        s.connect((IPaddr, port))

        data = s.recv(4096)
        dat = pickle.loads(data)

        #ss = input("enter name:")
        dat[player] = Players(0)

        dat = pickle.dumps(dat)
        s.send(dat)
