from NewCardGame.functions import *
import pygame
import os,sys
import random

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
BG = [pygame.image.load("Cards/table.jpg"),(0,0)]
WINDOW_CAPTION = pygame.display.set_caption("Durak Reborn 19.10.2019")

def shuffle(list):
    randomlist = []
    for q in range(len(list)):
        card = list.pop(random.randint(0, len(list) - 1))
        randomlist.append(card)
    return randomlist

def fill_defendlist():
    defend = []
    for i in range(50):
        defend.append('')

    for i in range(50):
        defend[i] = ''
    return defend

def suit(trumpcard):
    suit = ''
    for symbol in trumpcard:
        suit += symbol
        if symbol == "_":
            suit = ''

    return suit

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
             "Q_pik",])
OPP_HAND = []
TABLE = []
DEFEND = fill_defendlist()
print(DEFEND)
#MY_HAND = ["9_Bub","9_Kr","9_pik"]
MY_HAND = []

TRUMPCARD = CARD_LIST.pop(random.randint(0, len(CARD_LIST) - 1))
CARD_LIST.append(TRUMPCARD)
TRUMPSUIT = suit(TRUMPCARD)
COVER  = 'Card.jpg'

CARD_SIZE_MyHand = [125,100]
CARD_SIZE_OppHand = [125,100]
CARD_SIZE_Table = [125,100]
CARD_SIZE_DefList =  [125,100]
