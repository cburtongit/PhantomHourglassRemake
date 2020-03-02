import pygame
import pyganim
import sys
from datetime import date

# all my classes:
from Player import Player

WINDOW_X = 256*2
WINDOW_Y = 192*2

cur_date = date.today()


def main():
    # initialise pygame
    pygame.init()
    CLOCK = pygame.time.Clock()

    # setting up display properties
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    pygame.display.set_caption('Phantom Hourglass - ' + str(cur_date))

    # refresh rate of display
    screen_rate = 60

    background = pygame.transform.scale(pygame.image.load('resources/world/mercay_map.png'), (1024, 768)).convert()
    link = Player((WINDOW_X / 2), (WINDOW_Y / 2), 1, 'link', 100, 50, '', '', 5, 'left')

    # main loop here
    while 1:
        screen.blit(background, (link.Xpos, link.Ypos))
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
