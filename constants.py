from tkinter import Tk
from random import randint
import pygame

def shuffle(list):
    randomlist = []
    for q in range(len(list)):
        card = list.pop(randint(0, len(list) - 1))
        randomlist.append(card)
    return randomlist

def fill_defendlist():
    defend = []
    for i in range(50):
        defend.append('')

    for i in range(50):
        defend[i] = ''
    return defend

def card_suit(trumpcard):
    suit = ''
    for symbol in trumpcard:
        suit += symbol
        if symbol == "_":
            suit = ''

    return suit

root = Tk()
WINDOW_HEIGHT = root.winfo_screenheight()
WINDOW_WIDTH = root.winfo_screenwidth()

menu = True
game = True
collection = False
score = False
exit = False

WINDOW = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
BG = pygame.image.load("src/Other/table2.png")
WINDOW_CAPTION = pygame.display.set_caption("Durak Reborn 19.10.2019")

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
MY_HAND = []

TRUMPCARD = CARD_LIST.pop(randint(0, len(CARD_LIST) - 1))
CARD_LIST.append(TRUMPCARD)
TRUMPSUIT = card_suit(TRUMPCARD)
COVER = 'Card.jpg'

CARD_SIZE_MyHand = [125,100]
CARD_SIZE_OppHand = [125,100]
CARD_SIZE_Table = [125,100]
CARD_SIZE_DefList = [125,100]
