from NewCardGame.functions import card_balance,card_balanceBOT,events,update_window
import pygame

pygame.init()

card_balance()
card_balanceBOT()

def Durak():
    while True:
        events()
        update_window()

Durak()
