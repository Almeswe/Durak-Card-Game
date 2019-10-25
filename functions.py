from additional_functions import *
from constants import *
from time import sleep
import pygame
import sys

mydefend = False
bot_no_way = False
motion = False
dragging_card = None
draggingX = None
draggingY = None

def Menu(window,width,height):
    global game,menu,collection,score,exit

    window.blit(pygame.image.load("Cards/Menu.jpg"),(0,0))

    font = pygame.font.Font(None,150)
    smallfont = pygame.font.Font(None,20)
    menubarsfont = pygame.font.Font(None,35)

    AuthorText = smallfont.render("AlmesWe - 2019",1,(0,0,0))
    DurakText = font.render("Durak Game",1,(45,140,255))

    StartGameText = menubarsfont.render("Start Game",1,(0,0,0))
    CollectionText = menubarsfont.render("Collection",1,(0,0,0))
    ScoreText = menubarsfont.render("Score",1,(0,0,0))
    ExitText = menubarsfont.render("Exit",1,(0,0,0))

    margin_top = 13

    window.blit(StartGameText,(width//2.2,height//3+margin_top))
    window.blit(CollectionText,(width//2.2,height//3+50+margin_top))
    window.blit(ScoreText,(width//2.12,height//3+100+margin_top))
    window.blit(ExitText,(width//2.1,height//3+150+margin_top))

    window.blit(DurakText,(width//3.5,0))
    window.blit(AuthorText,(width-100,height-20))

    pygame.draw.rect(window, [87, 182, 4], (width / 2.38, height / 3, 220, 50), 5)
    pygame.draw.rect(window, [87, 182, 4], (width / 2.38, height / 3 + 50, 220, 50), 5)
    pygame.draw.rect(window, [87, 182, 4], (width / 2.38, height / 3 + 100, 220, 50), 5)
    pygame.draw.rect(window, [87, 182, 4], (width / 2.38, height / 3 + 150, 220, 50), 5)

    pygame.display.update()
    bool = True
    while bool:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    bool = False

                if event.type == pygame.MOUSEMOTION:
                    x,y = event.pos
                    if x in range(int(width/2.38),int(width/2.38+220)):

                        if y in range(int(height/3),int(height/3+50)):
                            pygame.draw.rect(window, [255,0,0], (width/2.38,height/3, 220, 50), 5)
                        else:
                            pygame.draw.rect(window, [87, 182, 4], (width/2.38,height/3, 220, 50), 5)

                        if y in range(int(height/3)+51, int(height/3)+100):
                            pygame.draw.rect(window, [255,0,0], (width/2.38,height/3+50, 220, 50), 5)
                        else:
                            pygame.draw.rect(window, [87, 182, 4], (width/2.38,height/3+50, 220, 50), 5)

                        if y in range(int(height/3)+101, int(height/3)+150):
                            pygame.draw.rect(window, [255,0,0], (width/2.38,height/3+100, 220, 50), 5)
                        else:
                            pygame.draw.rect(window, [87, 182, 4], (width/2.38,height/3+100, 220, 50), 5)

                        if y in range(int(height/3)+151, int(height/3)+200):
                            pygame.draw.rect(window, [255,0,0], (width/2.38,height/3+150, 220, 50), 5)
                        else:
                            pygame.draw.rect(window, [87, 182, 4], (width/2.38,height/3+150, 220, 50), 5)
                    else:
                        pygame.draw.rect(window, [87, 182, 4], (width / 2.38, height / 3, 220, 50), 5)
                        pygame.draw.rect(window, [87, 182, 4], (width / 2.38, height / 3 + 50, 220, 50), 5)
                        pygame.draw.rect(window, [87, 182, 4], (width / 2.38, height / 3 + 100, 220, 50), 5)
                        pygame.draw.rect(window, [87, 182, 4], (width / 2.38, height / 3 + 150, 220, 50), 5)


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x,y = event.pos
                        if x in range(int(width/2.38),int(width/2.38+220)):

                            if y in range(int(height/3),int(height/3+50)):

                                game = True
                                score = False
                                collection = False
                                exit = False
                                menu = False
                                card_balance()
                                card_balanceBOT()
                                pygame.display.update()
                                bool = False
                            if y in range(int(height/3)+51, int(height/3)+100):
                                game = False
                                score = False
                                collection = True
                                exit = False
                                menu = False
                                pygame.display.update()
                                bool = False
                            if y in range(int(height/3)+101, int(height/3)+150):
                                game = False
                                score = True
                                collection = False
                                exit = False
                                menu = False
                                pygame.display.update()
                                bool = False
                            if y in range(int(height/3)+151, int(height/3)+200):
                                sys.exit()

        pygame.display.update()

def Collection(window,width,height):
    global COVER
    global menu, start_game, exit, collection, score

    ColdCover = pygame.image.load("Cards/Covers/Cold.jpg")
    GoldCover = pygame.image.load("Cards/Covers/Gold.jpg")
    LavaCover = pygame.image.load("Cards/Covers/Lava.jpg")
    LoveCover = pygame.image.load("Cards/Covers/LoveisCost.jpg")
    NYCover = pygame.image.load("Cards/Covers/NY.jpg")
    RagnarosCover = pygame.image.load("Cards/Covers/Ragnaros.jpg")
    RubyCover = pygame.image.load("Cards/Covers/Ruby.jpg")
    StarCraftCover = pygame.image.load("Cards/Covers/StarCraft.jpg")
    TavernCover = pygame.image.load("Cards/Covers/Tavern.jpg")
    UngoroCover = pygame.image.load("Cards/Covers/Ungoro.jpg")
    StandartCover = pygame.image.load("Cards/Covers/Card.jpg")
    LegendaryCard = pygame.image.load("Cards/Covers/LegendaryCard.jpg")
    DalaranCard = pygame.image.load("Cards/Covers/Dalaran.png")

    font = pygame.font.Font(None,60)

    window.blit(pygame.image.load("Cards/Collection.jpg"),(0,0))
    window.blit(pygame.image.load("Cards/Buttons/back.png"),(0,height-50))

    window.blit(font.render("CURRENT COVER",1,(245,177,4)),(0,150))
    window.blit(pygame.image.load("Cards/Covers/"+COVER),(109,0))

    #covers
    #up
    window.blit(GoldCover,(WINDOW_WIDTH/3.2,300))
    window.blit(LavaCover,(WINDOW_WIDTH/3.2+100,300))
    window.blit(RagnarosCover,(WINDOW_WIDTH/3.2+200,300))
    window.blit(RubyCover,(WINDOW_WIDTH/3.2+300,300))
    window.blit(LegendaryCard,(WINDOW_WIDTH/3.2+400,300))
    window.blit(TavernCover,(WINDOW_WIDTH/3.2+500,300))
    #down
    window.blit(ColdCover,(WINDOW_WIDTH/3.2,450))
    window.blit(NYCover,(WINDOW_WIDTH/3.2+100,450))
    window.blit(LoveCover,(WINDOW_WIDTH/3.2+200,450))
    window.blit(StarCraftCover,(WINDOW_WIDTH/3.2+300,450))
    window.blit(DalaranCard,(WINDOW_WIDTH/3.2+400,450))
    window.blit(StandartCover,(WINDOW_WIDTH/3.2+500,450))
    #


    pygame.display.update()
    booll = True
    while booll:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                booll = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x,y = event.pos
                    if y in range (height-50,height):
                        if x in range(0,150):
                            menu = True
                            collection = False
                            booll = False
                            pygame.display.update()

                    if y in range(300,449):
                        if x in range(int(width/3.2),int(width/3.2+100)):
                            COVER = 'Gold.jpg'
                            window.blit(GoldCover, (109, 0))

                        if x in range(int(width/3.2)+100,int(width/3.2)+200):
                            COVER = 'Lava.jpg'
                            window.blit(LavaCover, (109, 0))

                        if x in range(int(width/3.2)+200,int(width/3.2)+300):
                            COVER = 'Ragnaros.jpg'
                            window.blit(RagnarosCover, (109, 0))

                        if x in range(int(width/3.2)+300,int(width/3.2)+400):
                            COVER = RubyCover
                            window.blit(RubyCover, (109, 0))

                        if x in range(int(width/3.2)+400,int(width/3.2)+500):
                            COVER = LegendaryCard
                            window.blit(LegendaryCard, (109, 0))

                        if x in range(int(width/3.2)+500,int(width/3.2)+600):
                            COVER = TavernCover
                            window.blit(TavernCover, (109, 0))

                        if x in range(int(width/3.2)+600,int(width/3.2)+700):
                            COVER = TavernCover
                            window.blit(TavernCover, (109, 0))

                    if y in range(450,600):
                        if x in range(int(width/3.2),int(width/3.2+100)):
                                COVER = ColdCover
                                window.blit(ColdCover, (109, 0))

                        if x in range(int(width/3.2)+100,int(WINDOW_WIDTH/3.2)+200):
                                COVER = NYCover
                                window.blit(NYCover, (109, 0))

                        if x in range(int(WINDOW_WIDTH/3.2)+200,int(width/3.2)+300):
                                COVER = LoveCover
                                window.blit(LoveCover, (109, 0))

                        if x in range(int(width/3.2)+300,int(width/3.2)+400):
                                COVER = StarCraftCover
                                window.blit(StarCraftCover, (109, 0))

                        if x in range(int(width/3.2)+400,int(width/3.2)+500):
                                COVER = DalaranCard
                                window.blit(DalaranCard, (109, 0))

                        if x in range(int(width/3.2)+500,int(width/3.2)+600):
                                COVER = StandartCover
                                window.blit(StandartCover, (109, 0))

            pygame.display.update()

def events():
    global motion,dragging_card
    global draggingX,draggingY
    global mydefend
    global TABLE,DEFEND

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            motion = True
            if event.button == 1:
                x, y = event.pos
                button_current_command(x, y,)
                try:
                    dragging_card = MY_HAND[find_card_position_onclick(x,y,CARD_SIZE_MyHand)]
                except:
                    dragging_card = None

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                x, y = event.pos
                find_defendcard_position_onclick(x, y, CARD_SIZE_Table[1], dragging_card,)

                motion = False
                draggingY = None
                draggingX = None
                dragging_card = None

        if motion:
            if event.type == pygame.MOUSEMOTION:
                draggingX,draggingY = event.pos

def check_winner(playersList):
    global CARD_LIST,MY_HAND,OPP_HAND,TABLE,game

    if len(playersList) == 0 and len(CARD_LIST) == 0:
        game = False

def update_window():
    global game,MY_HAND,OPP_HAND,DEFEND,TABLE,CARD_LIST,TRUMPCARD,mydefend
    global menu,score,collection,exit
    global bot_no_way,motion

    if menu:
        Menu(WINDOW,WINDOW_WIDTH,WINDOW_HEIGHT)

    elif collection:
        Collection(WINDOW,WINDOW_WIDTH,WINDOW_HEIGHT)

    elif game:
        check_winner(MY_HAND)
        check_winner(OPP_HAND)

        WINDOW.blit(BG, (0, 0))
        card_resizer()
        card_sorter(MY_HAND)
        card_sorter(OPP_HAND)

        draw_card_list()
        draw_buttons()
        button_visual_assistant()

        draw_cards(False)
        draw_dragged_card()

        if not game:
            menu = True
            game = False
            CARD_LIST = shuffle(["6_Bub",
                                 "6_heart",
                                 "6_Kr",
                                 "6_pik",
                                 "7_Bub",
                                 "7_heart",
                                 "7_Kr",
                                 "7_pik",
                                 "8_Bub",
                                 "8_heart",
                                 "8_Kr",
                                 "8_pik",
                                 "9_Bub",
                                 "9_heart",
                                 "9_Kr",
                                 "9_pik",
                                 "10_Bub",
                                 "10_heart",
                                 "10_Kr",
                                 "10_pik",
                                 "Ace_Bub",
                                 "Ace_heart",
                                 "Ace_Kr",
                                 "Ace_pik",
                                 "J_Bub",
                                 "J_heart",
                                 "J_Kr",
                                 "J_pik",
                                 "K_Bub",
                                 "K_heart",
                                 "K_Kr",
                                 "K_pik",
                                 "Q_Bub",
                                 "Q_heart",
                                 "Q_Kr",
                                 "Q_pik", ])
            OPP_HAND = []
            TABLE = []
            DEFEND = fill_defendlist()
            MY_HAND = []

            TRUMPCARD = CARD_LIST.pop(randint(0, len(CARD_LIST) - 1))
            CARD_LIST.append(TRUMPCARD)
            TRUMPSUIT = card_suit(TRUMPCARD)

            mydefend = False
            bot_no_way = False
            motion = False

    pygame.display.update()

def bot_action_defend():
    global OPP_HAND,TABLE,DEFEND,TRUMPSUIT
    global bot_no_way,mydefend

    if len(DEFEND) == 0:
        DEFEND = fill_defendlist()

    list = []
    for card in DEFEND:
        if card != '':
            list.append(card)

    beated = False

    if len(list) != 0 or len(TABLE) != 0:
        if len(list) == len(TABLE):
            mydefend = True
            card_balance()
            card_balanceBOT()
            TABLE = []
            DEFEND = []
            update_window()
            sleep(.3)
            bot_action_attack()

    if len(list) != 0 or len(TABLE) != 0:
        if mydefend == False:
            for tablecard in TABLE:
                for oppcard in OPP_HAND:
                    if DEFEND[TABLE.index(tablecard)] == '':
                            if card_suit(oppcard) == card_suit(tablecard):
                                if card_priority(oppcard) > card_priority(tablecard):
                                    OPP_HAND.pop(OPP_HAND.index(oppcard))
                                    DEFEND[TABLE.index(tablecard)] = oppcard
                                    update_window()
                                    beated = True

                            elif card_suit(oppcard) == TRUMPSUIT:
                                OPP_HAND.pop(OPP_HAND.index(oppcard))
                                DEFEND[TABLE.index(tablecard)] = oppcard
                                update_window()
                                beated = True

            for card in DEFEND:
                if card != '':
                    list.append(card)

            if not beated:
                    bot_no_way = True
            else:
                    print(list)
                    if len(TABLE) > 1:
                        cleartable = []
                        for tablecard in range(len(list)-1):
                            for clonecard in range(tablecard+1,len(list)-1):
                                print(list[tablecard],list[clonecard])
                                if list[tablecard] == list[clonecard]:
                                    list.pop(clonecard)
                                else:
                                    pass

                        print(list)

                        if len(list) != len(TABLE):
                            print(TABLE,list)
                            bot_no_way = True
                    else:
                        if len(list) != len(TABLE):
                            print(TABLE,list)
                            bot_no_way = True

def bot_action_attack():
        global OPP_HAND,TABLE,DEFEND,MY_HAND
        global mydefend

        list = []
        for card in DEFEND:
            if card != '':
                list.append(card)

        if len(DEFEND) == 0:
            DEFEND = fill_defendlist()
        nocards = True

        if len(TABLE) == 0:
            if len(OPP_HAND) != 0:
                nocards = False
                card = OPP_HAND.pop(0)
                TABLE.append(card)
                update_window()
                sleep(.2)
        if len(TABLE) != 0:
            for oppcard in OPP_HAND:
                for tablecard in TABLE:
                    if tablecard[0] == oppcard[0]:
                        if len(TABLE) < len(MY_HAND) + len(list):
                                nocards = False
                                OPP_HAND.pop(OPP_HAND.index(oppcard))
                                TABLE.append(oppcard)
                                update_window()
                                sleep(.2)
                                break

            for oppcard in OPP_HAND:
                for defcard in DEFEND+TABLE:
                    if defcard != '':
                        if defcard[0] == oppcard[0]:
                            if len(TABLE) < len(MY_HAND) + len(list):
                                nocards = False
                                OPP_HAND.pop(OPP_HAND.index(oppcard))
                                TABLE.append(oppcard)
                                update_window()
                                sleep(.2)
                                break

        if nocards == True:
            mydefend = False
            TABLE = []
            DEFEND = fill_defendlist()
            card_balanceBOT()
            card_balance()

def bot_action_toss():
    global TABLE,DEFEND,MY_HAND,OPP_HAND

    list = []
    for card in DEFEND:
        if card != '':
            list.append(card)

    if len(TABLE) != 0:
        for oppcard in OPP_HAND:
            for tablecard in TABLE:
                if tablecard[0] == oppcard[0]:
                    if len(TABLE) < len(MY_HAND) + len(list):
                            TABLE.append(oppcard)
                            OPP_HAND.pop(OPP_HAND.index(oppcard))
                            update_window()
                            sleep(.2)
                            break

        for oppcard in OPP_HAND:
            for defcard in DEFEND+TABLE:
                if defcard != '':
                    if defcard[0] == oppcard[0]:
                        if len(TABLE) < len(MY_HAND) + len(list):
                                OPP_HAND.pop(OPP_HAND.index(oppcard))
                                TABLE.append(oppcard)
                                update_window()
                                sleep(.2)
                                break

    MY_HAND += TABLE
    TABLE = []
    list = []
    for card in DEFEND:
        if card != '':
            list.append(card)
    DEFEND = list
    MY_HAND += DEFEND
    DEFEND = []

    card_balanceBOT()
    card_balance()

def button_visual_assistant():
    global TABLE,DEFEND,MY_HAND
    global mydefend

    list = []
    for card in DEFEND:
        if card != '':
            list.append(card)

    if mydefend:
        if len(list) == len(TABLE):
            if len(TABLE) != 0:
                pygame.draw.rect(WINDOW, (255, 0, 0), (200, 600, 100, 50), 5)

        for tablecard in TABLE:
            if tablecard == 'Ace_' + TRUMPSUIT:
                pygame.draw.rect(WINDOW, (255, 0, 0), (20, 600, 100, 50), 5)
    else:
        if len(list) + len(OPP_HAND) <= len(TABLE):
            pygame.draw.rect(WINDOW, (255, 0, 0), (200, 600, 100, 50), 5)
        if bot_no_way:
            pygame.draw.rect(WINDOW, (255, 0, 0), (20, 600, 100, 50), 5)

def button_current_command(x,y):
        global TABLE,DEFEND,MY_HAND,OPP_HAND
        global bot_no_way
        global mydefend

        if y in range(600,650):
            if x in range(20,120):
                pygame.draw.rect(WINDOW, (255, 0, 0), (20, 600, 100, 50),5)
                if mydefend:
                    #Беру все

                    #
                    bot_action_toss()
                    update_window()
                    sleep(.3)
                    bot_action_attack()
                    #

                else:
                    #Бери
                    if bot_no_way == True:
                        OPP_HAND += TABLE
                        TABLE = []
                        list = []
                        for card in DEFEND:
                            if card != '':
                                list.append(card)
                        DEFEND = list
                        OPP_HAND += DEFEND
                        DEFEND = []
                        bot_no_way = False
                        card_balance()
                        card_balanceBOT()

                    #
                    #MY ATTACK
                    #

            if x in range(200,300):
                if mydefend:
                    pygame.draw.rect(WINDOW, (255, 0, 0), (200, 600, 100, 50), 5)
                    #Я отбился
                    #
                    list = []
                    for card in DEFEND:
                        if card != '':
                            list.append(card)

                    if len(TABLE) != 0:
                        if len(TABLE) == len(list):
                            bot_action_attack()
                    #
                else:
                    pygame.draw.rect(WINDOW, (255, 0, 0), (200, 600, 100, 50), 5)
                    #Я походил
                    bot_action_defend()

def draw_buttons():
    global mydefend
    #525-675
    font_for_buttons = pygame.font.Font(None,20)
    pygame.draw.rect(WINDOW,(255,255,255),(20,600,100,50))
    pygame.draw.rect(WINDOW,(255,255,255),(200,600,100,50))
    pygame.draw.rect(WINDOW,(0,255,0),(20,600,100,50),5)
    pygame.draw.rect(WINDOW,(0,255,0),(200,600,100,50),5)

    if mydefend:
        #взять все,я походил,
        WINDOW.blit(font_for_buttons.render("Беру все",1,(9,76,152)),(35,617))
        WINDOW.blit(font_for_buttons.render("Я отбился",1,(9,76,152)),(215,617))
    else:
        #Бери,я все;
        WINDOW.blit(font_for_buttons.render("Бот берет",1,(9,76,152)),(35,617))
        WINDOW.blit(font_for_buttons.render("Я походил",1,(9,76,152)),(215,617))

def draw_dragged_card():
    global dragging_card
    global draggingX,draggingY
    if motion:
        try:
            WINDOW.blit(pygame.image.load("Cards/" + dragging_card + ".png"), (draggingX-50, draggingY-75))
            font = pygame.font.Font(None,50)
            if mydefend == False:
                pygame.draw.line(WINDOW,(0,0,0),(0,300),(WINDOW_WIDTH,300),3)
                pygame.draw.line(WINDOW,(0,0,0),(0,425),(WINDOW_WIDTH,425),3)

            elif mydefend:
                pygame.draw.line(WINDOW,(0,0,0),(0,400),(WINDOW_WIDTH,400),3)
                pygame.draw.line(WINDOW,(0,0,0),(0,525),(WINDOW_WIDTH,525),3)
                for line in range(len(TABLE)+1):
                    pygame.draw.line(WINDOW,(0,0,0),(CARD_SIZE_Table[1]*line,400),(CARD_SIZE_Table[1]*line,525),3)
        except:
            pass

def draw_card_list():
    global COVER,CARD_LIST,TRUMPCARD
    global WINDOW

    fontt = pygame.font.Font(None,30)

    if len(CARD_LIST) > 1:
        WINDOW.blit(pygame.image.load("Cards/"+TRUMPCARD+".png"),(1080,150))
        WINDOW.blit(pygame.image.load("Cards/Covers/"+COVER),(1100,100))
        WINDOW.blit(fontt.render(str(len(CARD_LIST)),1,(0,0,0)),(1100,90))

    if len(CARD_LIST) == 1:
        WINDOW.blit(pygame.image.load("Cards/"+TRUMPCARD+".png"),(1080,150))

def draw_cards(visible):
    global MY_HAND,OPP_HAND,TABLE,DEFEND

    counter = 0
    for card in MY_HAND:
        WINDOW.blit(pygame.image.load("Cards/"+card+".png"),(counter*CARD_SIZE_MyHand[1],WINDOW_HEIGHT-CARD_SIZE_MyHand[0]-50))
        counter += 1
    counter = 0
    for card in TABLE:
        WINDOW.blit(pygame.image.load("Cards/"+card+".png"),(counter*CARD_SIZE_Table[1],300))
        counter += 1
    counter = 0
    for card in OPP_HAND:
        if visible:
            WINDOW.blit(pygame.image.load("Cards/"+card+".png"),(counter*CARD_SIZE_OppHand[1],50))
        else:
            WINDOW.blit(pygame.image.load("Cards/Covers/"+COVER),(counter*CARD_SIZE_OppHand[1],50))
        counter += 1
    counter = 0
    for card in DEFEND:
        try:
            WINDOW.blit(pygame.image.load("Cards/"+card+".png"),(counter*CARD_SIZE_DefList[1],400))
        except:
            pass
        counter += 1

def card_resizer():
    global MY_HAND,OPP_HAND,TABLE,DEFEND
    global CARD_SIZE_MyHand,CARD_SIZE_DefList,CARD_SIZE_OppHand,CARD_SIZE_Table

    if len(MY_HAND) > 5:
        CARD_SIZE_MyHand = [125,70]
    if len(MY_HAND) > 10:
        CARD_SIZE_MyHand = [125, 50]
    if len(MY_HAND) > 15:
        CARD_SIZE_MyHand = [125, 30]
    if len(MY_HAND) <= 5:
        CARD_SIZE_MyHand = [125,100]

    if len(OPP_HAND) > 5:
        CARD_SIZE_OppHand = [125,70]
    if len(OPP_HAND) > 10:
        CARD_SIZE_OppHand = [125,50]
    if len(OPP_HAND) > 15:
        CARD_SIZE_OppHand = [125,30]
    if len(OPP_HAND) <= 5:
        CARD_SIZE_OppHand = [125,100]


    if len(TABLE) > 5:
        CARD_SIZE_Table = [125,70]
        CARD_SIZE_DefList = [125,70]
    if len(TABLE) > 10:
        CARD_SIZE_Table = [125,50]
        CARD_SIZE_DefList = [125,50]
    if len(TABLE) > 15:
        CARD_SIZE_Table = [125,30]
        CARD_SIZE_DefList = [125,30]
    if len(TABLE) <= 5:
        CARD_SIZE_Table = [125,100]
        CARD_SIZE_DefList = [125,100]

def card_sorter(list):
    for min in range(len(list) - 1):
        for j in range((min + 1), len(list)):
            if card_priority(list[min]) > card_priority(list[j]):
                list[j], list[min] = list[min], list[j]

def card_suit(card):
    suit = ''
    for symbol in card:
        suit += symbol
        if symbol == "_":
            suit = ''

    return suit

def card_priority(card):
    if card[0] == 'J':
        return 11
    elif card[0] == 'Q':
        return 12
    elif card[0] == 'K':
        return 13
    elif card[0] == 'A':
        return 14
    elif card[0] == '1':
        return 10
    else:
        return int(card[0])

def card_balance():
    global MY_HAND,CARD_LIST
    difference = 6 - len(MY_HAND)
    if difference > 0:
        for p in range(difference):
            if len(CARD_LIST) != 0:
                card = CARD_LIST.pop(0)
                MY_HAND.append(card)
                update_window()
                sleep(.1)

def card_balanceBOT():
    global OPP_HAND,CARD_LIST

    difference = 6 - len(OPP_HAND)
    if difference > 0:
        for p in range(difference):
            if len(CARD_LIST) != 0:
                card = CARD_LIST.pop(0)
                OPP_HAND.append(card)
                update_window()
                sleep(.1)

def find_card_position_onclick(x,y,card_width):

    if y in range(WINDOW_HEIGHT-CARD_SIZE_MyHand[0]-50,WINDOW_HEIGHT-50):
        floatCoordinateX = x / card_width[1]

        positionX = round(floatCoordinateX)

        if floatCoordinateX > positionX:
            pass
        else:
            positionX -= 1

        return positionX

def find_defendcard_position_onclick(x, y, card_width,card,):
        global TABLE, MY_HAND, DEFEND , mydefend

        floatCoordinateX = x / card_width

        posX = round(floatCoordinateX)

        if floatCoordinateX > posX:
            pass
        else:
            posX -= 1

        list = []
        for i in DEFEND:
            if i != '':
                list.append(i)

        if y >= 300 and y <= 425 and card != None:
            if mydefend == False:
                if len(TABLE) == 0:
                    MY_HAND.pop(MY_HAND.index(card))
                    TABLE.append(card)
                else:
                    found = False
                    for tablecard in TABLE:
                        if card[0] == tablecard[0]:
                            if len(OPP_HAND) + len(list) > len(TABLE):
                                MY_HAND.pop(MY_HAND.index(card))
                                TABLE.append(card)
                                found = True
                                break
                    if not found:
                        for defcard in DEFEND:
                            if defcard != '':
                                if card[0] == defcard[0]:
                                    if len(OPP_HAND) + len(list) > len(TABLE):
                                        MY_HAND.pop(MY_HAND.index(card))
                                        TABLE.append(card)
                                        break

        if y >= 400 and y <= 525:
            if mydefend:
                try:
                    if card_suit(TABLE[posX]) == card_suit(card):
                        if card_priority(card[0]) > card_priority(TABLE[posX]):
                            if DEFEND[posX] == '':
                                MY_HAND.pop(MY_HAND.index(card))
                                DEFEND[posX] = card
                    elif card_suit(card) == TRUMPSUIT:
                        if DEFEND[posX] == '':
                            MY_HAND.pop(MY_HAND.index(card))
                            DEFEND[posX] = card
                except:
                    pass
