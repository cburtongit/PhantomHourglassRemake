class Entity:
    # Coordinates X and Y are within game window, E indicates what level of elevation the Entity is on
    Xpos = 0
    Ypos = 0
    Epos = 0

    def __init__(self, x, y, e):
        self.Xpos = x
        self.Ypos = y
        self.Epos = e

    # for Camera movement for already moving enemies
    def offset(self, off_x, off_y):
        self.Xpos += off_x
        self.Ypos += off_y
