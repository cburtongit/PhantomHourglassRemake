import pygame
import pyganim
from Entity import Entity


class Player(Entity):
    # battle stats
    # health - total health, once 0 death() should be called
    health = 0
    # atk - amount of damage done to target
    atk = 0
    windUp = 0
    # what items the enemy has, should only have 1 or 2 unless boss, similar to player.inventory[]
    equipped = []

    # Inventory and Defense Items e.g. armor, shield
    # all items Entity is holding NON-EQUIPPED
    inventory = []

    # movement variables
    # moveUp = moveRight = moveDown = moveLeft = False
    direction = ''

    # animations
    test_img = pygame.image.load('resources/sprites/link/dev_link.png')

    def __init__(self, x, y, e, hpt, atk, inv, eqp, drc):
        super().__init__(x, y, e)
        self.health = hpt
        self.atk = atk
        self.windUp = 0
        self.inventory = inv
        self.equipped = eqp
        self.inventory = inv
        self.direction = drc

    def draw(self, drc, ):
        pass

    def draw(self, dis):
        dis.blit(self.test_img, (self.Xpos, self.Ypos))
