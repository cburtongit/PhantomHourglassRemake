import os
import sys
import random
import pygame
import pyganim
from Entity import Entity
from Player import Player


def main():
    # initialise pygame
    pygame.init()

    ## TEST ##
    screen = pygame.display.set_mode((512, 512))
    a = []
    b = []
    #player = Player(100, 100, 1, 1, 100, 100, a, b, 'left')
    background = pygame.image.load('resources/world/LTTP_start_house.png').convert()
    screen.blit(background, (0, 0))

    players = []
    for i in range(10):
        i = Player(random.randint(50, 450), random.randint(50, 450), 1, i, 100, 50, '', '', 5, 'left')
        players.append(i)
    while 1:
        screen.blit(background, (0, 9))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for i in players:
            i.draw(screen, 'down')
        pygame.display.update()
        pygame.time.delay(100)

    ## TEST ##


# if __name__ == main:
#    main()

main()
pygame.quit()
