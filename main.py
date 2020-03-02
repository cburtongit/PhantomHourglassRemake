import sys
import pygame
import pyganim
from Entity import Entity
from Player import Player


def main():
    # initialise pygame
    pygame.init()
    clock = pygame.time.Clock();

    # setting up display properties
    screen = pygame.display.set_mode((512, 512))
    pygame.display.set_caption(('Phantom Hourglass - alpha build'))

    # refresh rate of display
    screenRate = 60



    # TEST

    player = Player(100, 100, 0)
    # TEST


if __name__ == main:
    main()
