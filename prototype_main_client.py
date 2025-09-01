import socket
import pickle

FORMAT = 'utf-8'
HEADER = 64




class Main:

    def __init__(self,player):
        self.s = socket.socket()
        host = socket.gethostname()
        self.player = player
        IPaddr = '26.4.87.63'
        port = 60070
        self.s.connect((IPaddr, port))


    def snd(self,data):
        message = data.encode(FORMAT)
        self.s.send(message)
        #print("sending...:", data)

    def start(self):
        #name = input("Enter name:")
        self.snd(self.player)

        da = self.s.recv(1024)
        do = pickle.loads(da)
        return(do)


    def round_client(self):
        self.snd(self.player)
        p = self.s.recv(1024)
        dd = pickle.loads(p)
        return dd






class Game_Main:
    def __init__(self,player):
        self.s = socket.socket()
        host = socket.gethostname()
        self.player = player
        IPaddr = '26.4.87.63'
        port = 60071
        self.s.connect((IPaddr, port))
        lis = pickle.loads(self.s.recv(2048))
        lis.append(self.player)
        self.s.send(pickle.dumps(lis))
        self.d = None
        self.decided = False
        self.current = None
        self.winner = None
        self.lop = []
        self.trump = self.revealed = self.starting = None
        

    def send_card(self,player, card):
        d = {player : card}
        dd= pickle.dumps(d)
        self.s.send(dd)

    def recieve_card(self):
        d = pickle.loads(self.s.recv(2048))
        return d
    def ask_trump(self):
        d = {self.player: "ask trump?"}
        self.s.send(pickle.dumps(d))
    def trump_client(self,player, trump_card):
        d = {player: trump_card}
        dd = pickle.dumps(d)
        self.s.send(dd)

    def sand(self):
        d = {self.player: "cani ?"}
        self.s.send(pickle.dumps(d))


    def keep_recv(self):
        while True:
            dat = self.s.recv(4295)
            try:
                self.d = dat.decode()
                if self.d == "trump reveal!!":
                    self.revealed = True

            except:
                self.d = pickle.loads(dat)
                if self.decided == False:
                    if self.d[1]:
                        self.trump = self.d[0]
                        self.decided = True
                    if len(self.d) == 2:
                        self.s.send(pickle.dumps({self.player: "roundover"}))
                else:
                    if "cani ?" not in self.d.values():
                        #if
                        if self.starting == None:
                            self.starting = self.d
                        self.current = self.d
                        self.lop.append(self.current)
                    self.s.send(pickle.dumps({self.player: "roundover"}))

                    if "winner" in self.d.keys():

                        self.winner = self.d
                        self.lop = []
                        self.starting = None

            print("from keep recv", self.d)
            print(len(self.lop))
