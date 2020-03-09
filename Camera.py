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
        target = self.target
        if event.type == pygame.KEYDOWN:
            # escape key quits game
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            # movement based on keypress
            # UP
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.direction = self.UP
                self.moveup = True
                self.movedown = False
                if self.target is not None:
                    target.direction = target.UP
                    target.moveup = True
                    target.movedown = False
            # DOWN
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.direction = self.DOWN
                self.moveup = False
                self.movedown = True
                if self.target is not None:
                    target.direction = target.DOWN
                    target.moveup = False
                    target.movedown = True
            # LEFT
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.direction = self.LEFT
                self.moveleft = True
                self.moveright = False
                if self.target is not None:
                    target.direction = target.LEFT
                    target.moveleft = True
                    target.moveright = False
            # RIGHT
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.direction = self.RIGHT
                self.moveleft = False
                self.moveright = True
                if self.target is not None:
                    target.direction = target.RIGHT
                    target.moveleft = False
                    target.moveright = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.moveup = False
                if self.moveleft:
                    self.direction = self.LEFT
                if self.moveright:
                    self.direction = self.RIGHT
                if self.target is not None:
                    if self.moveleft:
                        target.direction = target.LEFT
                    if self.moveright:
                        target.direction = target.RIGHT
            # DOWN
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.movedown = False
                if self.moveleft:
                    self.direction = self.LEFT
                if self.moveright:
                    self.direction = self.RIGHT
                if self.target is not None:
                    if self.moveleft:
                        target.direction = target.LEFT
                    if self.moveright:
                        target.direction = target.RIGHT
            # LEFT
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.moveleft = False
                if self.moveup:
                    self.direction = self.UP
                if self.movedown:
                    self.direction = self.DOWN
                if self.target is not None:
                    if self.moveup:
                        target.direction = target.UP
                    if self.movedown:
                        target.direction = target.DOWN
            # RIGHT
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.moveright = False
                if self.moveup:
                    self.direction = self.UP
                if self.movedown:
                    self.direction = self.DOWN
                if self.target is not None:
                    if self.moveup:
                        target.direction = target.UP
                    if self.movedown:
                        target.direction = target.DOWN

    def move(self):
        target = self.target
        # UP
        self.old_x = self.Xpos
        self.old_y = self.Ypos
        if self.moveup:
            self.Ypos -= self.speed
            self.hit_box.move_ip(0, -self.speed)
            if self.target is not None:
                target.Ypos -= target.speed
                target.hit_box.move_ip(0, -target.speed)
        # DOWN
        if self.movedown:
            self.Ypos += self.speed
            self.hit_box.move_ip(0, +self.speed)
            if self.target is not None:
                target.Ypos += target.speed
                target.hit_box.move_ip(0, +target.speed)
        # LEFT
        if self.moveleft:
            self.Xpos -= self.speed
            self.hit_box.move_ip(-self.speed, 0)
            if self.target is not None:
                target.Xpos -= target.speed
                target.hit_box.move_ip(-target.speed, 0)
        # RIGHT
        if self.moveright:
            self.Xpos += self.speed
            self.hit_box.move_ip(+self.speed, 0)
            if self.target is not None:
                target.Xpos += target.speed
                target.hit_box.move_ip(+target.speed, 0)

    def get_offset(self):
        offset = [(self.old_x - self.Xpos), (self.old_y, self.Ypos)]
        return offset
