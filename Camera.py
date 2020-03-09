import pygame
from Entity import Entity


class Camera(Entity):

    speed = 2.5

    LEFT, RIGHT, UP, DOWN = 'left right up down'.split()
    direction = DOWN

    moveup = movedown = moveleft = moveright = False

    hit_box = None

    target = None

    old_x = 0
    old_y = 0

    def __init__(self, x, y, e, target):
        super().__init__(x, y, e)
        self.Xpos = x
        self.Ypos = y
        self.Epos = e
        self.target = target
        self.hit_box = pygame.Rect((self.Xpos, self.Ypos), (32, 32))

        self.old_x = self.Xpos
        self.old_y = self.Ypos

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

    def move(self):
        # UP
        self.old_x = self.Xpos
        self.old_y = self.Ypos
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

    def get_offset(self):
        offset = [(self.old_x - self.Xpos), (self.old_y, self.Ypos)]
        return offset
