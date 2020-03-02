import pygame
import pyganim


class Entity:
    # Coordinates X and Y are within game window, E indicates what level of elevation the Entity is on
    Xpos = 0
    Ypos = 0
    Epos = 0

    # entity id, for collision checking
    ent_id = 0

    def __init__(self, x, y, e, ent_id):
        self.Xpos = x
        self.Ypos = y
        self.Epos = e
        self.ent_id = ent_id

    def check_collide(self):
        pass
