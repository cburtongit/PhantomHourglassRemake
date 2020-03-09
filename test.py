import pygame
import sys
from datetime import date

# all my classes:
from Player import Player
from Tile import *
from Camera import Camera

SCALER = 4
WINDOW_X = 1600
WINDOW_Y = 900
# creates 4:3 aspect ratio - floor division for int

cur_date = date.today()

mapData = [
    # 0 - 7
    '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '01', '00', '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '01', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '01', '00', '00',
    '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00',
    # 8 - 15
    '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '01', '00', '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '01', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '01', '00', '00',
    '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00',
    # 16 - 24
    '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '01', '00', '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '01', '00', '00', '00', '00', '00', '00', '00', '00', '01', '00', '00', '00', '00', '01', '00', '00',
    '00', '00', '00', '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00']

# initialise Pygame
pygame.init()
clock = pygame.time.Clock()

# setting up display properties
display = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
pygame.display.set_caption('The Legend of Zelda: Phantom Past - ' + str(cur_date))
screen = pygame.Surface((342, 192))

# refresh rate of display
screen_rate = 60

# debug: background loading to see sprite errors
background = pygame.transform.scale(pygame.image.load('resources/placeholder.png'), (1024, 768)).convert()


def load_world(map_data):
    tiles_x = 0
    tiles_y = 0
    tiles_count = 0
    tiles = []

    for i in map_data:
        if i == '00':
            i = Tile(tiles_x, tiles_y, 0, False, False, 'resources/sprites/island/water/water1.png')
            tiles.append(i)
        elif i == '01':
            i = Tile(tiles_x, tiles_y, 0, False, False, 'resources/sprites/island/water/water2.png')
            i.make_solid()
            tiles.append(i)
        tiles_x += 32
        tiles_count += 1
        if tiles_count >= 43:
            tiles_x = 0
            tiles_y += 32
            tiles_count = 0
    return tiles


def main():
    link = Player((WINDOW_X / 2), (WINDOW_Y / 2), 0)
    camera = Camera(link.Xpos, link.Ypos, 0, link)

    # load the map data
    tiles = load_world(mapData)

    # main loop
    while 1:
        for event in pygame.event.get():
            # link.get_input(event)
            camera.get_input(event)
            if event.type == pygame.QUIT:
                sys.exit()

        # MOVEMENT
        # link.move()
        camera.move()
        for i in tiles:
            i.offset(camera.get_offset_x(), camera.get_offset_y())

        # COLLISION

        # DRAW
        screen.blit(background, (0, 0))
        for i in tiles:
            i.draw(screen)
        # draw to half of the surface - 16 pixels so sprite lines up with center
        link.draw(screen, 155, 80)

        #  ENGINE UPDATE
        scale_screen = pygame.transform.scale(screen, (WINDOW_X, WINDOW_Y))
        display.blit(scale_screen, (0, 0))
        pygame.display.update()
        clock.tick(screen_rate * 0.5)

        # debug
        # print(link.direction + camera.direction)
        print(
            'Link: ' + str(link.Xpos) + ', ' + str(link.Ypos) + '\nCamera: ' + str(camera.Xpos) + ', ' + str(
                camera.Ypos))
        '''
        print('RECT for LINK (top): ' + str(link.hit_box.topleft) + ', ' + str(
            link.hit_box.topright) + '   RECT for CAMERA (top): ' + str(camera.hit_box.topleft) + ', ' + str(
            camera.hit_box.topright))
        print('RECT for LINK (bottom): ' + str(link.hit_box.bottomleft) + ', ' + str(
            link.hit_box.bottomright) + '   RECT for CAMERA (bottom): ' + str(camera.hit_box.bottomleft) + ', ' + str(
            camera.hit_box.bottomright))
        '''


main()
