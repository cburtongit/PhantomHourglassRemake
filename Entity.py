class Entity:
    # Coordinates X and Y are within game window, E indicates what level of elevation the Entity is on
    Xpos = 0
    Ypos = 0
    Epos = 0

    def __init__(self, x, y, e):
        self.Xpos = x
        self.Ypos = y
        self.Epos = e

    def check_collide(self):
        pass

    # for Camera movement for already moving enemies
    def offset(self, offset):
        self.Xpos += offset[0]
        self.Ypos += offset[1]
