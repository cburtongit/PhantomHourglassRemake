import pygame
import pyganim
from Entity import Entity


class Tile(Entity):
    # determines if the object can be walked over
    solid = False
    img = None
    # create variable for rectangle for later
    hit_box = None
    # determines if the tile is animated
    animated = False

    def __init__(self, x, y, e, solid, anime, img):
        super().__init__(x, y, e)
        self.solid = solid
        self.animated = anime
        self.img = pygame.image.load(img)
        self.hit_box = pygame.Rect((self.Xpos, self.Ypos), (32, 32))

    def draw(self, dis):
        dis.blit(self.img, (self.hit_box.left, self.hit_box.top))

    def is_solid(self):
        if self.solid:
            return True
        else:
            return False

    def is_animated(self):
        if self.animated:
            return True
        else:
            return False


class AnimatedTile(Tile):
    frames = []
    frame_conductor = None

    def __init__(self, frames):
        self.frames = frames
        self.frame_conductor = pyganim.PygConductor(frames)

    def draw(self, dis):
        self.frame_conductor.play()
        self.frames.blit(dis, (self.Xpos, self.Ypos))
