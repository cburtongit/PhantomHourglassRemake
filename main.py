import pygame
import pyganim
import sys
from datetime import date

# all my classes:
from Player import Player

WINDOW_X = 512
WINDOW_Y = 512

cur_date = date.today()


def main():
    # initialise pygame
    pygame.init()
    clock = pygame.time.Clock()

    # setting up display properties
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    pygame.display.set_caption('Phantom Hourglass - ' + str(cur_date))

    # refresh rate of display
    screen_rate = 60

    # main loop here


if __name__ == main:
    main()
