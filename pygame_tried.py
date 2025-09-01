class Sprite(pygame.sprite.Sprite):
    def __init__(self, card, no):
        super().__init__()
        self.card = card
        lis = []


        e = str(card.suit[0]).lower() + str(card.value)
        self.image = pygame.image.load(f"./Cards/{e}.png").convert_alpha()
        #self.image.fill((0,0,0))
        lis.append(self.image)
        plus = 0
        for i in range(len(lis)):

            if no == 0:
                p = 225 + plus
                start = (p, 50)

            if no == 1:
                p = 150 + plus
                lis[i] = pygame.transform.rotozoom(lis[i], 90, 1)
                start = (675, p)
            if no == 2:
                p = 225 + plus
                start = (p, 500)

            if no == 3:
                p = 150 + plus
                lis[i] = pygame.transform.rotozoom(lis[i], 90, 1)
                start = (50, p)
            plus += 50

            self.rect = lis[i].get_rect(topleft = start )

    def mouse_input(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("upd")
                if self.rect.collidepoint(event.pos):
                    print("ha")
                    tup = pygame.mouse.get_pos()
                    self.rect.y = tup[1]
                    self.rect.x = tup[0]

    def update(self):
        self.mouse_input()



im = pygame.image.load("card_clubs_03.png")
brg = pygame.image.load("download.png").convert_alpha()
brg.get_rect()
#brg  = pygame.transform.rotozoom(brg, 60, 1)
screen.blit(brg, (0,0))
sprites = pygame.sprite.Group()
for i in range(len(name_list)):
    for e in name_list[i].card:
        # print("wjshfjuef", e)
        c = Sprite(e, i)
        sprites.add(c)