import time
import random

class Cards(object):
    def __init__(self, suit, value):
        try:
            self.value = value.upper()
        except:
            pass
        self.suit = suit
        self.value = value
        self.worth = 0
        if value == 3:
            self.worth = 5
        elif value == "J":
            self.worth = 3
        elif value == 9:
            self.worth = 2
        elif value == "A":
            self.worth = 1.01
        elif value == 10:
            self.worth = 1
        elif value == "K":
            self.worth = 0

    @staticmethod
    def Shuffle(name_list):
        vals = (3, "J", 9, "A", 10, "K")
        suits = ("Spade", "Club", "Heart", "Diamond")
        all_cards = []
        while len(all_cards) <= 23:
            va = Cards(random.choice(suits), random.choice(vals))
            if va in all_cards:
                pass
            else:
                all_cards.append(va)

        for i in name_list:
            print(i)
            while len(name_list[i]) <= 5:
                a = random.choice(all_cards)
                all_cards.remove(a)
                try:
                    name_list[i].append(a)
                except:
                    pass
                print(a)
    @staticmethod
    def max_cards(player):

        suit_no = {"Heart":0,"Diamond":0,"Spade":0,"Club":0}
        for i in range(len(player)):
            if player[i].suit in suit_no.keys():
                suit_no[player[i].suit] += 1+ player[i].worth/100
                #card = player[i]

        Valmax = max(suit_no.values())
        Keymax = max(suit_no, key= lambda x: suit_no[x])
        card = player.find_card(Keymax)
        return (Keymax,Valmax,card )

    def short(self):
        stri = str(self.suit[0]).lower() + str(self.value)
        return stri

    def __eq__(self, other):
        if f'({self.suit}, {self.value})' == other :
            return True
        else:
            return False
    def __str__(self):
        self.cards = f'({self.suit}, {self.value})'
        return self.cards





class Round_bot:
    def __init__(self, rounde):
        self.starting_player = name_list[0]
        self.current_player = name_list[1]
        self.bot_player = name_list[1:]
        straight = name_list[0]

        if rounde == 1:
            #self.decide_trump()
            self.current_player.worthe()
            name_list[1].is_trump = True
            if self.current_player in self.bot_player:
                if int(self.current_player.worth) >=30:
                    print("jackpot")
                    print(f'Trump decided: {Cards.max_cards(self.current_player)[0]}, worth:{self.current_player.worth}')
                    self.current_player.trump_card = Cards.max_cards(self.current_player)
                    print(self.current_player.trump_card[2])
                else:
                    print(f'Trump decided: {Cards.max_cards(self.current_player)[0]}, worth:{self.current_player.worth}')
                    self.current_player.trump_card = Cards.max_cards(self.current_player)
                    print(self.current_player.trump_card[2])
        elif rounde == "winner":
            pass
        else:
            self.round_start()
    def round_start(self):
            sus = ["Spade", "Club", "Heart", "Diamond"]
            choic = random.choice(sus)
            sus.remove(choic)
            print("The suit for the round is:", choic)
            self.current_suit = choic
            print('------------------',"          ", "------------------")
            lis = {}
            for i in range(len(name_list)):

                    possession = False
                    if possession:
                        #print(name_list[i])
                        played_card =name_list[i].play_card(self.current_suit)

                    if not possession:
                        #print(name_list[i])
                        played_card = name_list[i].play_card(self.current_suit, suit=self.current_suit)
                        lis[name_list[i]] =played_card.worth

                    print(f"p{i} plays {played_card}!!!")
                    ma = max(lis.values())
                    possession = max(lis, key= lambda x: lis[x]).poss



    def decide_trump(self):
        while True:

            print("decide trunp")


class Round:
    def __init__(self,round):
        if round == 1:
            self.decide_trunp()

    def decide_trump(self):
        pass
class Players:

    def __init__(self,team):
        self.current = 0
        self.card = []
        self.is_trump = False
        self.trump_card = []
        self.poss = False
        self.team = team
        self.name = self


    def trumpify(self, suit):
        for i in self.card:
            if i.suit == suit:
                i.worth += 10
    def append(self, item):
        self.card.append(item)

    def worthe(self):
        no_of_suit = Cards.max_cards(self)
        val = 0
        for i in self.card:
            val += i.worth

        worth = (no_of_suit[1]*6)+(val)

        self.worth = worth
        return worth

    def play_card(self, played=None, suit =None):
        play = None
        self.trump_revealed = False
        turn = 1

        if suit != None:
            try:
                play = self.min_card(suit)
            except ValueError:
                if play == None:
                    played = self.no_card()
                if play == None and self.trump_revealed == True:
                    play = self.no_card_trump(played)


            turn += 1
        if play == None:
            played = self.no_card()

        if play == None and self.trump_revealed == True:
            play = self.no_card_trump(played)

        return play

    def no_card_trump(self, played):
        play = None
        player_card = self.card
        player = 0

        for i in range(0,len(player_card)-1):

            new_worth = old_worth = 0
            if player_card[i].suit == played:

                new_worth = (player_card[i].worth)

                if new_worth > old_worth:
                    play = player_card[i]

                else:
                    play = player_card[i]

            old_worth = player_card[i].worth
            player += 1
        try:
            self.card.remove(play)
        except:
            pass
        if play == None:
            play = random.choice(self.card)
            self.card.remove(play)
        return play
    def no_card(self):
        print("not there")
        play = None
        player_card = self.card
        for i in name_list:
            if i.is_trump == True:
                trump_card = i.trump_card[0]
                print("Trump suite is:", trump_card)
                #play = i.trump_card[2]
                #player_card.remove(play)
                played = i.trump_card[0]
        self.trump_revealed = True
        return played
    def find_card(self, suit = None, val = None, worth  = None):
        e =[]
        for i in self.card:
            if i.suit == suit:
                f = i
            if i.value == val:
                e.append(val)

        return f
    def min_card(self, suit):
        player = self.card
        lis = {}
        for i in range(len(player)):
            if player[i].suit == suit:
                lis[player[i].suit] = player[i].worth

        Keymin = min(lis, key=lis.get)
        card = self.find_card(Keymin)
        player.remove(card)
        return (card)






    def __iter__(self):
        return self
    def __len__(self):
        e = 0
        for i in self.card:
            e+= 1
        return e

    def __next__(self):
        if self.current >= len(self.card):
            raise StopIteration

        self.current += 1
        return self.card
    def __getitem__(self, item):
        return self.card[item]

    def __str__(self):
        self.car = "["
        for i in self.card:
            self.car += f'{i.cards}, '
        self.car += "]"
        return self.car


"""
p1 = Players(0)
p2 = Players(1)
p3 = Players(0)
p4 = Players(1)

name_list = [p1, p2, p3, p4]

Cards.Shuffle(name_list = name_list)


Rounds(1)
i = 2

while True:

    '''
    Rounds(i)
    print(i)
    time.sleep(3)
    i += 1
    if i > 7:
        break
        i = 2
        print("new---------------------new-------------------------new")
        Cards.Shuffle(name_list=name_list)
        Rounds(1)'''
"""





