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
    # movement speed
    speed = 2.5

    # Inventory and Defense Items e.g. armor, shield
    # all items Entity is holding NON-EQUIPPED
    inventory = []

    # movement variables
    # moveUp = moveRight = moveDown = moveLeft = False

    LEFT, RIGHT, UP, DOWN = 'left right up down'.split()
    direction = DOWN

    moveup = movedown = moveleft = moveright = False

    hit_box = ''

    # animations
    # test_img = pygame.image.load('resources/sprites/link/dev_link.png')
    up_sprites = pygame.image.load('resources/sprites/link/link_up.png')
    down_sprites = pygame.image.load('resources/sprites/link/link_down.png')
    right_sprites = pygame.image.load('resources/sprites/link/link_right.png')
    # mirrored right-facing sprites
    left_sprites = pygame.transform.flip(pygame.image.load('resources/sprites/link/link_right.png'), True, False)

    # walking sprites animations
    link_sprites = {'UP': pyganim.PygAnimation([('resources/sprites/link/link_up.png', 100),
                                              ('resources/sprites/link/link_up1.png', 100),
                                              ('resources/sprites/link/link_up2.png', 100),
                                              ('resources/sprites/link/link_up3.png', 100),
                                              ('resources/sprites/link/link_up4.png', 100),
                                              ('resources/sprites/link/link_up5.png', 100),
                                              ('resources/sprites/link/link_up6.png', 100),
                                              ('resources/sprites/link/link_up7.png', 100)]),
                    'DOWN': pyganim.PygAnimation([('resources/sprites/link/link_down.png', 100),
                                                ('resources/sprites/link/link_down1.png', 100),
                                                ('resources/sprites/link/link_down2.png', 100),
                                                ('resources/sprites/link/link_down3.png', 100),
                                                ('resources/sprites/link/link_down4.png', 100),
                                                ('resources/sprites/link/link_down5.png', 100),
                                                ('resources/sprites/link/link_down6.png', 100),
                                                ('resources/sprites/link/link_down7.png', 100)]),
                    'RIGHT': pyganim.PygAnimation([('resources/sprites/link/link_right.png', 100),
                                                 ('resources/sprites/link/link_right1.png', 100),
                                                 ('resources/sprites/link/link_right2.png', 100),
                                                 ('resources/sprites/link/link_right3.png', 100),
                                                 ('resources/sprites/link/link_right4.png', 100),
                                                 ('resources/sprites/link/link_right5.png', 100),
                                                 ('resources/sprites/link/link_right6.png', 100),
                                                 ('resources/sprites/link/link_right7.png', 100)]),
                    'LEFT': pyganim.PygAnimation([('resources/sprites/link/link_right.png', 100),
                                                 ('resources/sprites/link/link_right1.png', 100),
                                                 ('resources/sprites/link/link_right2.png', 100),
                                                 ('resources/sprites/link/link_right3.png', 100),
                                                 ('resources/sprites/link/link_right4.png', 100),
                                                 ('resources/sprites/link/link_right5.png', 100),
                                                 ('resources/sprites/link/link_right6.png', 100),
                                                 ('resources/sprites/link/link_right7.png', 100)]),
                    }
    # inverting RIGHT sprites to get LEFT facing ones
    link_sprites['LEFT'].flip(True, False)
    link_sprites['LEFT'].makeTransformsPermanent()
    # conductor object controls animations easier
    link_conductor = pyganim.PygConductor(link_sprites)

    def __init__(self, x, y, e, ent_id, hpt, atk, inv, eqp, speed, drc):
        super().__init__(x, y, e, ent_id)
        self.health = hpt
        self.atk = atk
        self.windUp = 0
        self.inventory = inv
        self.equipped = eqp
        self.inventory = inv
        # directional variables
        self.direction = drc
        self.moveleft = False
        self.moveright = False
        self.moveup = False
        self.movedown = False
        # hitbox for the player, used in collision
        self.hit_box = pygame.Rect((self.Xpos + 8, self.Ypos + 8), (16, 16))

    def draw(self, dis):
        # PLAY animation and draw correct animation for direction
        if self.moveleft or self.moveright or self.moveup or self.movedown:
            self.link_conductor.play()
            if self.direction == self.UP:
                self.link_sprites['UP'].blit(dis, (self.Xpos, self.Ypos))
            if self.direction == self.DOWN:
                self.link_sprites['DOWN'].blit(dis, (self.Xpos, self.Ypos))
            if self.direction == self.RIGHT:
                self.link_sprites['RIGHT'].blit(dis, (self.Xpos, self.Ypos))
            if self.direction == self.LEFT:
                self.link_sprites['LEFT'].blit(dis, (self.Xpos, self.Ypos))
        # STOP animation and draw idle sprite for last direction
        else:
            self.link_conductor.stop()
            if self.direction == self.UP:
                dis.blit(self.up_sprites, (self.Xpos, self.Ypos))
            if self.direction == self.DOWN:
                dis.blit(self.down_sprites, (self.Xpos, self.Ypos))
            if self.direction == self.RIGHT:
                dis.blit(self.right_sprites, (self.Xpos, self.Ypos))
            if self.direction == self.LEFT:
                dis.blit(self.left_sprites, (self.Xpos, self.Ypos))

    def move(self):
        # UP
        if self.moveup:
            self.Ypos -= self.speed
            self.hit_box.move_ip(0, -self.speed)
        # DOWN
        if self.movedown:
            self.Ypos += self.speed
            self.hit_box.move_ip(0, +self.speed)
        # LEFT
        if self.moveleft:
            self.Xpos -= self.speed
            self.hit_box.move_ip(-self.speed, 0)
        # RIGHT
        if self.moveright:
            self.Xpos += self.speed
            self.hit_box.move_ip(+self.speed, 0)

    def get_input(self, event):
        if event.type == pygame.KEYDOWN:
            print("KEY PRESSED")
            # escape key quits game
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            # movement based on keypress
            # UP
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.direction = self.UP
                self.moveup = True
                self.movedown = False
            # DOWN
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.direction = self.DOWN
                self.moveup = False
                self.movedown = True
            # LEFT
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.direction = self.LEFT
                self.moveleft = True
                self.moveright = False
            # RIGHT
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.direction = self.RIGHT
                self.moveleft = False
                self.moveright = True

        elif event.type == pygame.KEYUP:
            print('KEY NOT PRESSED')
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.moveup = False
                if self.moveleft:
                    self.direction = self.LEFT
                if self.moveright:
                    self.direction = self.RIGHT
            # DOWN
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.movedown = False
                if self.moveleft:
                    self.direction = self.LEFT
                if self.moveright:
                    self.direction = self.RIGHT
            # LEFT
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.moveleft = False
                if self.moveup:
                    self.direction = self.UP
                if self.movedown:
                    self.direction = self.DOWN
            # RIGHT
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.moveright = False
                if self.moveup:
                    self.direction = self.UP
                if self.movedown:
                    self.direction = self.DOWN

    def hurt(self, damage):
        self.health -= damage
        if self.health < 1:
            self.kill()

    def attack(self):
        pass

    def attack(self):
        pass

    def use_item(self):
        pass

    def kill(self):
        pass
