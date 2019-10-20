from NewCardGame.constants import *
import pygame
import sys,os
import time
import random

mydefend = False
botBool = False
motion = False
dragging_card = None
draggingX = None
draggingY = None
gameOver = False

def events():
    global motion,dragging_card
    global draggingX,draggingY
    global mydefend
    global TABLE,DEFEND


    k = pygame.key.get_pressed()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            motion = True
            if event.button == 1:
                x, y = event.pos
                button_command(x, y, mydefend, True)
                try:
                    dragging_card = MY_HAND[find_object(x,y,CARD_SIZE_MyHand,WINDOW_HEIGHT)]
                except:
                    dragging_card = None

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                x, y = event.pos
                find_object_board(x, y, CARD_SIZE_Table[1], dragging_card,mydefend)

                motion = False
                draggingY = None
                draggingX = None
                dragging_card = None

        if motion:
            if event.type == pygame.MOUSEMOTION:
                draggingX,draggingY = event.pos
        else:
            if event.type == pygame.MOUSEMOTION:
                X,Y = event.pos
                hover_effect(X, Y)

def bot_defend():
    global OPP_HAND,TABLE,DEFEND,TRUMPSUIT
    global botBool,mydefend

    if len(DEFEND) == 0:
        DEFEND = fill_defendlist()

    list = []
    for card in DEFEND:
        if card != '':
            list.append(card)

    if len(list) != 0 or len(TABLE) != 0:
        beated = False
    else:
        beated = True

    if len(list) != 0 or len(TABLE) != 0:
        if len(list) == len(TABLE):
            mydefend = True
            card_balance(MY_HAND,CARD_LIST)
            card_balanceBOT(OPP_HAND,CARD_LIST)
            TABLE = []
            DEFEND = []
            update_window()
            time.sleep(.3)
            bot_action(True)

    if len(list) != 0 or len(TABLE) != 0:
        if mydefend == False:
            for oppcard in OPP_HAND:
                for tablecard in TABLE:
                    if DEFEND[TABLE.index(tablecard)] == '':
                        if suit(oppcard) == suit(tablecard):
                            if priority(oppcard) > priority(tablecard):
                                OPP_HAND.pop(OPP_HAND.index(oppcard))
                                DEFEND[TABLE.index(tablecard)] = oppcard
                                update_window()
                                beated = True
                                break
                        elif suit(oppcard) == TRUMPSUIT:
                            OPP_HAND.pop(OPP_HAND.index(oppcard))
                            DEFEND[TABLE.index(tablecard)] = oppcard
                            update_window()
                            beated = True
                            break

    if beated == False:
        botBool = True

def bot_action(boolean):
    global OPP_HAND,TABLE,DEFEND,MY_HAND
    global mydefend

    list = []
    for card in DEFEND:
        if card != '':
            list.append(card)

    if boolean == True:
        if len(DEFEND) == 0:
            DEFEND = fill_defendlist()
        nocards = True

        if len(TABLE) == 0:
            if len(OPP_HAND) != 0:
                nocards = False
                card = OPP_HAND.pop(0)
                TABLE.append(card)
                update_window()
                time.sleep(.2)
        if len(TABLE) != 0:
            for oppcard in OPP_HAND:
                for tablecard in TABLE:
                    if tablecard[0] == oppcard[0]:
                        if len(TABLE) < len(MY_HAND) + len(list):
                                nocards = False
                                OPP_HAND.pop(OPP_HAND.index(oppcard))
                                TABLE.append(oppcard)
                                update_window()
                                time.sleep(.2)
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
                                time.sleep(.2)
                                break

        if nocards == True:
            mydefend = False
            TABLE = []
            DEFEND = fill_defendlist()
            card_balanceBOT(OPP_HAND,CARD_LIST)
            card_balance(MY_HAND,CARD_LIST)
    else:
        bot_toss()

def bot_toss():
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
                            time.sleep(.2)
                            break

        for oppcard in OPP_HAND:
            for defcard in DEFEND+TABLE:
                if defcard != '':
                    if defcard[0] == oppcard[0]:
                        if len(TABLE) < len(MY_HAND) + len(list):
                                OPP_HAND.pop(OPP_HAND.index(oppcard))
                                TABLE.append(oppcard)
                                update_window()
                                time.sleep(.2)
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

    card_balanceBOT(OPP_HAND, CARD_LIST)
    card_balance(MY_HAND, CARD_LIST)

def button_helper():
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
        if botBool:
            pygame.draw.rect(WINDOW, (255, 0, 0), (20, 600, 100, 50), 5)


def button_command(x,y,mydefend,click):
    global TABLE,DEFEND,MY_HAND,OPP_HAND
    global botBool

    if click:
        if y in range(600,650):
            if x in range(20,120):
                pygame.draw.rect(WINDOW, (255, 0, 0), (20, 600, 100, 50),5)
                if mydefend:
                    #Беру все

                    #
                    bot_action(False)
                    update_window()
                    time.sleep(.3)
                    bot_action(True)
                    #

                else:
                    #Бери
                    if botBool == True:
                        OPP_HAND += TABLE
                        TABLE = []
                        list = []
                        for card in DEFEND:
                            if card != '':
                                list.append(card)
                        DEFEND = list
                        OPP_HAND += DEFEND
                        DEFEND = []
                        botBool = False
                        card_balance(MY_HAND,CARD_LIST)
                        card_balanceBOT(OPP_HAND,CARD_LIST)

                    #
                    #MY ATTACK
                    #

            if x in range(200,300):
                pygame.draw.rect(WINDOW, (255, 0, 0), (200, 600, 100, 50), 5)
                if mydefend:
                    #Я отбился
                    #
                    list = []
                    for card in DEFEND:
                        if card != '':
                            list.append(card)

                    if len(TABLE) != 0:
                        if len(TABLE) == len(list):
                            bot_action(True)
                    #
                else:
                    #Я походил
                    bot_defend()

def draw_buttons(mydefend):
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

def resize():
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

def draw_cards(myhand,opphand,table,defend,visible):
    counter = 0
    for card in myhand:
        WINDOW.blit(pygame.image.load("Cards/"+card+".png"),(counter*CARD_SIZE_MyHand[1],WINDOW_HEIGHT-CARD_SIZE_MyHand[0]))
        counter += 1
    counter = 0
    for card in table:
        WINDOW.blit(pygame.image.load("Cards/"+card+".png"),(counter*CARD_SIZE_Table[1],300))
        counter += 1
    counter = 0
    for card in opphand:
        if visible:
            WINDOW.blit(pygame.image.load("Cards/"+card+".png"),(counter*CARD_SIZE_OppHand[1],0))
        else:
            WINDOW.blit(pygame.image.load("Cards/Covers/"+COVER),(counter*CARD_SIZE_OppHand[1],0))
        counter += 1
    counter = 0
    for card in defend:
        try:
            WINDOW.blit(pygame.image.load("Cards/"+card+".png"),(counter*CARD_SIZE_DefList[1],400))
        except:
            pass
        counter += 1


def find_object(x,y,card_width,height):

    if y >= height-card_width[0]:
        floatCoordinateX = x / card_width[1]

        positionX = round(floatCoordinateX)

        if floatCoordinateX > positionX:
            pass
        else:
            positionX -= 1

        return positionX

def card_balance(myhand,list):
    difference = 6 - len(myhand)
    if difference > 0:
        for p in range(difference):
            if len(list) != 0:
                card = list.pop(0)
                myhand.append(card)
                update_window()
                time.sleep(.1)

def card_balanceBOT(opphand,list):
    difference = 6 - len(opphand)
    if difference > 0:
        for p in range(difference):
            if len(list) != 0:
                card = list.pop(0)
                opphand.append(card)
                update_window()
                time.sleep(.1)

def sort(myhand):
    for min in range(len(myhand) - 1):
        for j in range((min + 1), len(myhand)):
            if priority(myhand[min]) > priority(myhand[j]):
                myhand[j], myhand[min] = myhand[min], myhand[j]

def suit(trumpcard):
    suit = ''
    for symbol in trumpcard:
        suit += symbol
        if symbol == "_":
            suit = ''

    return suit

def priority(card):
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

def hover_effect(x,y):
    global TABLE, MY_HAND, DEFEND
    floatCoordinateX = x / CARD_SIZE_MyHand[1]
    posX = round(floatCoordinateX)
    if floatCoordinateX > posX:
        pass
    else:
        posX -= 1

    if y in range(WINDOW_HEIGHT-125,WINDOW_HEIGHT):
        if x in range(CARD_SIZE_MyHand[1]*posX,CARD_SIZE_MyHand[1]*posX+CARD_SIZE_MyHand[1]):
            print(CARD_SIZE_MyHand[1]*posX,CARD_SIZE_MyHand[1]*posX+CARD_SIZE_MyHand[1])
            try:
                WINDOW.blit(pygame.image.load("Cards/"+MY_HAND[posX]+'.png'),(posX*CARD_SIZE_MyHand[1],WINDOW_HEIGHT-125))
            except:
                pass

def find_object_board(x,y,card_width,card,mydefend):
        global TABLE,MY_HAND,DEFEND

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
                            if len(OPP_HAND)+len(list) > len(TABLE):
                                MY_HAND.pop(MY_HAND.index(card))
                                TABLE.append(card)
                                found = True
                                break
                    if not found:
                        for defcard in DEFEND:
                            if defcard != '':
                                if card[0] == defcard[0]:
                                    if len(OPP_HAND)+len(list) > len(TABLE):
                                        MY_HAND.pop(MY_HAND.index(card))
                                        TABLE.append(card)
                                        break

        if y >= 400 and y <= 525:
            if mydefend:
                try:
                    if suit(TABLE[posX]) == suit(card):
                        if priority(card[0]) > priority(TABLE[posX]):
                            if DEFEND[posX] == '':
                                MY_HAND.pop(MY_HAND.index(card))
                                DEFEND[posX] = card
                    elif suit(card) == TRUMPSUIT:
                        if DEFEND[posX] == '':
                            MY_HAND.pop(MY_HAND.index(card))
                            DEFEND[posX] = card
                except:
                    pass


def draw_dragged_card():
    global dragging_card
    global draggingX,draggingY
    if motion:
        try:
            WINDOW.blit(pygame.image.load("Cards/" + dragging_card + ".png"), (draggingX, draggingY))
            font = pygame.font.Font(None,50)
            if mydefend == False:
                pygame.draw.line(WINDOW,(0,0,0),(0,300),(WINDOW_WIDTH,300),3)
                pygame.draw.line(WINDOW,(0,0,0),(0,425),(WINDOW_WIDTH,425),3)
                #WINDOW.blit(font.render("|PUT CARDS HERE|",1,(255,255,255)),(400,345))
            elif mydefend:
                pygame.draw.line(WINDOW,(0,0,0),(0,400),(WINDOW_WIDTH,400),3)
                pygame.draw.line(WINDOW,(0,0,0),(0,525),(WINDOW_WIDTH,525),3)
                for line in range(len(TABLE)+1):
                    pygame.draw.line(WINDOW,(0,0,0),(CARD_SIZE_Table[1]*line,400),(CARD_SIZE_Table[1]*line,525),3)
                #WINDOW.blit(font.render("|PUT CARDS HERE|",1,(255,255,255)),(400,445))

        except:
            pass


def check_winner(playersList):
    global CARD_LIST,MY_HAND,OPP_HAND,TABLE,gameOver

    if len(playersList) == 0 and len(CARD_LIST) == 0:
        print("Winner->",str(playersList))
        gameOver = True

def update_window():
    if not gameOver:

        check_winner(MY_HAND)
        check_winner(OPP_HAND)

        WINDOW.blit(BG[0],BG[1])
        resize()
        sort(MY_HAND)
        sort(OPP_HAND)

        draw_card_list()
        draw_buttons(mydefend)
        button_helper()

        draw_cards(MY_HAND,OPP_HAND,TABLE,DEFEND,False)
        draw_dragged_card()

        pygame.display.update()
    else:
        time.sleep(5)
        sys.exit()
