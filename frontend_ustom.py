import pickle
import socket
import threading
import time
import random
import customtkinter as ctk
from PIL import Image
import init_client as pc
import prototype_main_client as mew
import  prototye_Round_cleint as prc


player = input("Enter name:")
round = 0
first_round_done = False
class Main_Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        sides = ["blank", "left", "top", "right"]
        res = ["blank", (400,100), (100,600), (400,100)]

        self.d = {}
        if int(player) +1 > 4:
            e = 1
        else:
            e = int(player) + 1
        for i in range(1,4):
            self.d["f"+str(i)] = Cards_image(self, card = blank, side = sides[i], height=res[i][0], width=res[i][1], numb= e)
            if e >= 4:
                e = 1
            elif e < 4:
                e+=1

        self.d["Bottom_Frame"] = Cards_image(self, card=cas, side="bottom", height=100, width=600, numb = int(player))


        self.Board_frame = Board_Frame(self, height = 400, width= 600)
        self.mainloop()

    def __str__(self):
        return("Windiw")


class Trump_Card:
    def __init__(self, player, trump_card):
        print(player, ":", trump_card)
        connect_game.trump_client(player, trump_card)



class Board_Frame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.man(parent)
        self.old = None
        self.plus = 0
        self.winner = None
        self.cando = False

    def man(self, parent):
        card = connect_game.current
        winner = connect_game.winner
        reveal = connect_game.revealed

        if reveal != None:
            if self.cando != reveal:
                car = parent.d["Bottom_Frame"].Card_buttons(parent = self, card = connect_game.trump.short(), side = "left", rot= "pe")
                car.place(relx = 0.5, rely = 0.5, anchor = "center")
                self.cando = reveal

        #print(card)
        if winner != None:
            #print("winner")
            if self.winner != winner:
                mew = parent.d["Bottom_Frame"].Card_buttons(parent=self, card=blank[0], side="left", rot="als")
                for p in parent.d:
                    w = parent.d[p]
                    if str(w.numb) in winner:
                        print("in")
                        if w.side == "top":
                            x = 100 + self.plus
                            y = -20
                        elif w.side == "left":
                            x = -20
                            y = 100 + self.plus
                        elif w.side == "right":
                            x = 570
                            y = 100 + self.plus
                        elif w.side == "bottom":
                            print("bot")
                            x = 100 + self.plus
                            y = 300
                        mew.place(x = x, y = y)

                self.plus += 20
                self.winner = winner

        if card != None:
            #print("insied")
            if self.old != card:
                for i in card:
                    if i != player:
                        casss = parent.d["Bottom_Frame"].Card_buttons(parent=self, card=card[i].short(), side="left", rot="als")
                        for p in parent.d:
                            w =parent.d[p]
                            if str(w.numb) in card.keys():
                                print("ye")
                                if w.side == "top":
                                    x = 250
                                    y = 30
                                elif w.side == "left":
                                    x = 30
                                    y = 180
                                elif w.side == "right":
                                    x = 600 - 90
                                    y = 180
                                casss.place(x= x, y = y)




                self.place(relx=0.5, rely=0.5, anchor="center")
                self.old = card

        parent.after(ms = 100, func = lambda: self.man(parent))
    def __str__(self):
        return("froame")


class Cards_image(ctk.CTkFrame):
    def __init__(self, parent, card, side, numb, **kwargs):
        super().__init__(parent, **kwargs)
        self.numb = numb
        lo = []
        #print(cas)
        self.side = side
        play = ctk.CTkLabel(self, text = str(numb), width = 20, height = 20)
        play.place(relx = 1, rely = 0, anchor ="e" )
        for i in cas.card:
            r = str(i.suit[0]).lower() + str(i.value).lower()
            #print(r)
            lo.append(r)

        self.par = parent
        plus = 0
        y = 0
        d = {}
        main = {}
        if side == "top":
            self.anc = "n"
            for i in card:
                y =+ plus
                main["group" + str(i)] = self.Card_buttons(parent=self, card=i, side=side)
                main["group" + str(i)].place(x=y, y=1)
                plus += 100
            self.place(relx =0.5 , rely = 0, anchor = "n")

        e = 0
        if side == "bottom":
            for i in lo:
                y =+ plus
                d["grup" + str(i)] = self.Card_buttons(parent=self, card=i,obj =card[e] , side=side)
                d["grup" + str(i)].place(x=y, y=1)
                card[e]
                plus += 100
                e +=1
            self.place(relx=0.5, rely=1, anchor="s")


        elif side == "left" :
            for i in card:
                y =+ plus
                d["group" + str(i)] = self.Card_buttons(parent=self, card=i, side=side)
                d["group" + str(i)].place(x=1, y=y)
                plus += 68
            self.place(relx =0 , rely = 0.5, anchor = "w")

        if side =="right":
            for i in card:
                y =+ plus
                d["group" + str(i)] = self.Card_buttons(parent=self, card=i, side=side)
                d["group" + str(i)].place(x=1, y=y)
                plus += 68
            self.place(relx =1 , rely = 0.5, anchor = "e")


    def pla(self, card):
        if self.side == "left":
            card.place(x=30, y=180)

        if self.side == "top":
            print("top")
        if self.side == "right":
            print("right")


    def Card_buttons(self,card, parent, side,obj= None, rot = None):
        global round
        deg = 0
        raw_img =Image.open(f"./Cards/{card}.png")

        if side == "left":
            #print(side)
            deg = 90

        elif side == "right":
            deg= 90

        if rot != None:
            deg = random.randint(0,180)


        img = ctk.CTkImage(raw_img.rotate(deg), size=(64, 64))
        but =ctk.CTkLabel(parent, image = img, text = "", width= 64, height=64)

        but.bind('<Button-1>', lambda event: self.move_card(but, side, card, obj))

        return but
    def filter(self, but):
        #print("he")
        connect_game.sand()
        time.sleep(0.5)
        print(connect_game.d)
        return connect_game.d
            #print(dic)

    def trump_decider(self,obj):
        trump = obj
        Trump_Card(player, trump)
        return trump
    def move_card(self, card, side, card_str,obj):
        global round

        response = self.filter(card)

        if response == "trump?":
            #print("trump?")
            connect_game.send_card(player,obj)
        if response == "yes":

            if side == "bottom":
                x = 250
                y= 400-90
                #connect_game.send_card(player, obj)
                casp = connect_game.starting
                print(casp)
                is_there = False
                if casp == None:
                    self.place_card(card, card_str, side, obj, x , y)
                else:
                    for i in casp:
                        for e in cas.card:
                            if e.suit == casp[i].suit:
                                is_there = True
                        if is_there:
                            if casp[i].suit == obj.suit:
                                self.place_card(card, card_str, side, obj, x , y)
                            elif casp[i].suit != obj.suit:
                                print("cant play")
                        elif is_there == False:
                            print("you dont have that suit", "ASK TRUMP")

                            Trump = connect_game.trump

                            connect_game.ask_trump()
                            if obj.suit == Trump.suit:
                                self.place_card(card, card_str, side, obj, x , y)

                            if obj.suit != Trump.suit:
                                print("not the right card")
        elif response =="no":
            print("not your turn")

    def __str__(self):
        return str("frame")

    def place_card(self, card, card_str, side, obj , x , y):
        card.place_forget()
        card = self.Card_buttons(parent=self.par.Board_frame, card=card_str, side=side, rot="als")
        connect_game.send_card(player, obj)
        cas.card.remove(obj)
        card.place(x=x, y=y)
#init.py
pc.main(player)
input("Ready?")
connect = mew.Main(player) #prototype_main
cas = connect.start()  #recieveing a crad
print(cas)
blank = []
for i in range(0,6):
    blank.append("blank")

print("staring round client")



connect_game = mew.Game_Main(player)
threading.Thread(target= connect_game.keep_recv ).start()
Main_Window()