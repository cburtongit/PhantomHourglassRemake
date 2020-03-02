import sys
import pygame
from datetime import date

from Player import Player

WINDOW_X = 512
WINDOW_Y = 512

cur_date = date.today()


def main():
    pygame.init()

    CLOCK = pygame.time.Clock()
    pygame.display.set_caption('Phantom Hourglass ALPHA - ' + str(cur_date))
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    background = pygame.image.load('resources/world/LTTP_start_house.png').convert()
    screen.blit(background, (0, 0))

    link = Player((WINDOW_X / 2), (WINDOW_Y / 2), 1, 'link', 100, 50, '', '', 5, 'left')
    while 1:
        screen.blit(background, (0, 9))
        for event in pygame.event.get():
            link.get_input(event)
            if event.type == pygame.QUIT:
                sys.exit()

        print(link.direction)
        link.move()
        link.draw(screen)

        pygame.display.update()
        CLOCK.tick(30)


main()
pygame.quit()
