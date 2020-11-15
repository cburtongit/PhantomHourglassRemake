import pygame
import sys
from datetime import date

# all my classes:
from Player import Player
from Tile import *
from Camera import Camera

SCALER = 4
WINDOW_X = 342
WINDOW_Y = 192
# creates 4:3 aspect ratio - floor division for int

cur_date = date.today()

mapData = [
    # 0 - 7
    '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01',
    '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01',
    '01', '01', '01', '01', '01',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    # 8 - 15
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '00', '00', '00', '00', '01',
    # 16 - 24
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
    '01', '00', '00', '00', '01',
    '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01',
    '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01',
    '01', '01', '01', '01', '01',
    ]

# initialise Pygame
pygame.init()
clock = pygame.time.Clock()

# setting up display properties
display = pygame.display.set_mode((WINDOW_X * SCALER, WINDOW_Y * SCALER))
pygame.display.set_caption('The Legend of Zelda: Sands to the Past - ' + str(cur_date))
screen = pygame.Surface((WINDOW_X, WINDOW_Y))

# refresh rate of display
screen_rate = 120

# debug: background loading to see sprite errors
background = pygame.transform.scale(pygame.image.load('resources/placeholder.png'), (1024, 768)).convert()


def load_world(map_data):
    # Tiles are generated by
    tiles_x = 0
    tiles_y = 0
    tiles_count = 0
    tiles = []
    solid_tiles = []

    for i in map_data:
        if i == '00':
            i = Tile(tiles_x, tiles_y, 0, False, False, 'resources/sprites/island/water/water1.png')
            tiles.append(i)
        elif i == '01':
            i = Tile(tiles_x, tiles_y, 0, False, False, 'resources/sprites/island/water/water2.png')
            i.make_solid()
            tiles.append(i)
            solid_tiles.append(i)
        tiles_x += 32
        tiles_count += 1
        if tiles_count >= 43:
            tiles_x = 0
            tiles_y += 32
            tiles_count = 0
    return tiles, solid_tiles


def check_collision(ent_a, ent_b):
    if ent_a.hit_box.colliderect(ent_b.hit_box):
        return True


def get_collision_direction(target, ent):
    # TOP - LINK COLLIDES FACING DOWN
    if target.hit_box.midtop[1] > ent.hit_box.midtop[1]:
        return 'down'
    # LEFT - LINK COLLIDES FACING RIGHT
    elif target.hit_box.midleft[0] > ent.hit_box.midleft[0]:
        return 'right'
    # RIGHT - LINK COLLIDES FACING LEFT
    elif target.hit_box.midright[0] < ent.hit_box.midright[0]:
        return 'left'
    # BOTTOM - LINK COLLIDES FACING UP
    else:
        return 'up'


def main():
    link = Player(155, 96, 0)
    camera = Camera(0, link)

    # load the map data
    tiles, solid_tiles = load_world(mapData)

    # main loop
    while 1:
        # INPUT
        for event in pygame.event.get():
            camera.get_input(event)
            if event.type == pygame.QUIT:
                sys.exit()

        # MOVEMENT
        camera.move()
        for i in tiles:
            i.offset(camera.get_offset())

        for tile in solid_tiles:
            if check_collision(link, tile):
                for i in tiles:
                    i.offset(camera.get_offset_inverted())
                print("LINK collides with " + str(tile))

        # DRAW
        screen.blit(background, (0, 0))
        for i in tiles:
            i.draw(screen)
        # draw to half of the surface - 16 pixels so sprite lines up with center
        link.draw(screen, 155, 96)

        #  ENGINE UPDATE
        scaled_screen = pygame.transform.scale(screen, (WINDOW_X * SCALER, WINDOW_Y * SCALER))
        display.blit(scaled_screen, (0, 0))
        pygame.display.update()
        clock.tick(screen_rate * 0.5)

        # debug
        print('LINK: ' + str(link.hit_box.topleft) + ', ' + str(link.hit_box.topright) + ', '
              + str(link.hit_box.bottomleft) + ', ' + str(link.hit_box.bottomright))

main()
