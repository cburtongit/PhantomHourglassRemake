import pygame
import Entity


class Monster(Entity):
    # battle stats
    # health - total health, once 0 death() should be called
    health = 0
    # atk - amount of damage done to target
    atk = 0
    windUp = 0

    # what items the enemy has, should only have 1 or 2 unless boss, similar to player.inventory[]
    equipped = []

    # loyalty determines interaction with other Entities - 0 - player; 1 - phantom; 2 - neutral;
    loyalty = 0

    # hostile to the player or player-loyal Entities - 0 - not hostile; 1 - hostile to player ONLY; 2 - hostile to all;
    hostile = 0

    # movement variables
    # moveUp = moveRight = moveDown = moveLeft = False
    direction = ''

    # current sprite set to draw
    currentSprite = {}

    def __init__(self, x, y, e, health, atk, windUp, inv, drc):
        super().__init__(x, y, e)
        self.health = health
        self.atk = atk
        self.windUp = windUp
        self.inventory = inv
        self.direction = drc
