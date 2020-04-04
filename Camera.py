import pygame
from Entity import Entity


class Camera(Entity):

    LEFT, RIGHT, UP, DOWN = 'left right up down'.split()
    direction = DOWN
    x_direction = LEFT
    y_direction = DOWN

    moveup = movedown = moveleft = moveright = False

    target = None

    old_x = 0
    old_y = 0

    speed = 0

    def __init__(self, e, target):
        self.target = target
        super().__init__(target.Xpos, target.Ypos, e)
        self.Epos = e
        self.old_x = self.Xpos
        self.old_y = self.Ypos
        self.speed = target.speed

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
                self.y_direction = self.UP
                self.moveup = True
                self.movedown = False
                if self.target is not None:
                    target.direction = target.UP
                    target.moveup = True
                    target.movedown = False
            # DOWN
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.direction = self.DOWN
                self.y_direction = self.DOWN
                self.moveup = False
                self.movedown = True
                if self.target is not None:
                    target.direction = target.DOWN
                    target.moveup = False
                    target.movedown = True
            # LEFT
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.direction = self.LEFT
                self.x_direction = self.LEFT
                self.moveleft = True
                self.moveright = False
                if self.target is not None:
                    target.direction = target.LEFT
                    target.moveleft = True
                    target.moveright = False
            # RIGHT
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.direction = self.RIGHT
                self.x_direction = self.RIGHT
                self.moveleft = False
                self.moveright = True
                if self.target is not None:
                    target.direction = target.RIGHT
                    target.moveleft = False
                    target.moveright = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.moveup = False
                target.moveup = False
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
                target.movedown = False
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
                target.moveleft = False
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
                target.moveright = False
                if self.moveup:
                    self.direction = self.UP
                if self.movedown:
                    self.direction = self.DOWN
                if self.target is not None:
                    if self.moveup:
                        target.direction = target.UP
                    if self.movedown:
                        target.direction = target.DOWN

    """
    def move(self):
        target = self.target
        # UP
        self.old_x = self.Xpos
        self.old_y = self.Ypos
        if self.moveup:
            self.Ypos -= self.speed
            #self.hit_box.move_ip(0, -self.speed)
            if self.target is not None:
                target.Ypos -= self.speed
                target.hit_box.move_ip(0, -self.speed)
        # DOWN
        if self.movedown:
            self.Ypos += self.speed
            #self.hit_box.move_ip(0, +self.speed)
            if self.target is not None:
                target.Ypos += self.speed
                target.hit_box.move_ip(0, +self.speed)
        # LEFT
        if self.moveleft:
            self.Xpos -= self.speed
            #self.hit_box.move_ip(-self.speed, 0)
            if self.target is not None:
                target.Xpos -= self.speed
                target.hit_box.move_ip(-self.speed, 0)
        # RIGHT
        if self.moveright:
            self.Xpos += self.speed
            #self.hit_box.move_ip(+self.speed, 0)
            if self.target is not None:
                target.Xpos += self.speed
                target.hit_box.move_ip(+self.speed, 0)
    """

    def move(self):
        self.old_x = self.Xpos
        self.old_y = self.Ypos
        # UP
        if self.moveup:
            self.Ypos -= self.speed
        # DOWN
        if self.movedown:
            self.Ypos += self.speed
        # LEFT
        if self.moveleft:
            self.Xpos -= self.speed
        # RIGHT
        if self.moveright:
            self.Xpos += self.speed

    def get_offset(self):
        offset = list([])
        offset.append(self.old_x - self.Xpos)
        offset.append(self.old_y - self.Ypos)
        return offset

    def get_offset_x(self):
        return self.old_x - self.Xpos

    def get_offset_y(self):
        return self.old_y - self.Ypos

    def get_offset_inverted(self):
        offset = list([])
        offset.append(~(self.old_x - self.Xpos) + 1)
        offset.append(~(self.old_y - self.Ypos) + 1)
        return offset
