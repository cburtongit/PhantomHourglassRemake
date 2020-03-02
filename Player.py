import pygame
# import pyganim
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
    # movement speed
    speed = 5

    # Inventory and Defense Items e.g. armor, shield
    # all items Entity is holding NON-EQUIPPED
    inventory = []

    # movement variables
    # moveUp = moveRight = moveDown = moveLeft = False
    direction = ''

    moveup = movedown = moveleft = moveright = False

    # animations
    test_img = pygame.image.load('resources/sprites/link/dev_link.png')
    up_sprites = [pygame.image.load('resources/sprites/link/link_up.png')]
    down_sprites = [pygame.image.load('resources/sprites/link/link_down.png')]
    right_sprites = [pygame.image.load('resources/sprites/link/link_right.png')]
    # mirrored right-facing sprites
    left_sprites = [pygame.transform.flip(pygame.image.load('resources/sprites/link/link_right.png'), True, False)]

    def __init__(self, x, y, e, ent_id, hpt, atk, inv, eqp, speed, drc):
        super().__init__(x, y, e, ent_id)
        self.health = hpt
        self.atk = atk
        self.windUp = 0
        self.inventory = inv
        self.equipped = eqp
        self.inventory = inv

        self.direction = drc

        self.moveleft = False
        self.moveright = False
        self.moveup = False
        self.movedown = False

    def draw(self, dis):
        # dis.blit(self.test_img, (self.Xpos, self.Ypos))
        if self.direction == 'up':
            dis.blit(self.up_sprites[0], (self.Xpos, self.Ypos))
        if self.direction == 'down':
            dis.blit(self.down_sprites[0], (self.Xpos, self.Ypos))
        if self.direction == 'right':
            dis.blit(self.right_sprites[0], (self.Xpos, self.Ypos))
        if self.direction == 'left':
            dis.blit(self.left_sprites[0], (self.Xpos, self.Ypos))

    def move(self):
        if self.moveup:
            self.Ypos -= self.speed
        if self.movedown:
            self.Ypos += self.speed
        if self.moveleft:
            self.Xpos -= self.speed
        if self.moveright:
            self.Xpos += self.speed

    def getInput(self, event):
        if event.type == pygame.KEYDOWN:
            print("KEY PRESSED")
            # escape key quits game
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            # movement based on keypress
            # UP
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.direction = UP
                self.moveup = True
                self.movedown = False
                self.move()
            # DOWN
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.direction = DOWN
                self.moveup = False
                self.movedown = True
                self.move()
            # LEFT
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.direction = LEFT
                self.moveleft = True
                self.moveright = False
                self.move()
            # RIGHT
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.direction = RIGHT
                self.moveleft = False
                self.moveright = True
                self.move()

        elif event.type == pygame.KEYUP:
            print('KEY NOT PRESSED')
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.moveup = False
            # DOWN
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.movedown = False
            # LEFT
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.moveleft = False
            # RIGHT
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.moveright = False
