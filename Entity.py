import pygame


class Entity:
    # Coordinates X and Y are within game window, E indicates what level of elevation the Entity is on
    Xpos = 0
    Ypos = 0
    Epos = 0

    hit_box = None

    def __init__(self, x, y, e):
        self.Xpos = x
        self.Ypos = y
        self.Epos = e
        self.hit_box = pygame.Rect((self.Xpos, self.Ypos), (32, 32))

    # for Camera movement for already moving enemies
    def offset(self, offset):
        self.Xpos += offset[0]
        self.Ypos += offset[1]
        self.hit_box.move_ip(offset[0], offset[1])
