import pygame


class World:
    w_name = ''
    bg_img = ''
    X_win = 0
    Y_win = 0
    screen = None

    def __init__(self, world_name, img, x, y):
        self.w_name = world_name
        self.bg_img = pygame.image.load(img)
        self.X_win = x
        self.Y_win = y
        self.screen = pygame.display.set_mode((X_win, Y_win))

    def draw(self):
        pass


