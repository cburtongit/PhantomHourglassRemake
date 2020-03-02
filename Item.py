import pygame


class Item:
    #
    name = ''
    # indicates what kind of item:
    # 0 - quest item;
    # 1 - weapon;
    # 2 - consumables;
    # 3 - collectibles;
    # 4 - trading;
    # 5 - ship parts
    type = 0
    # defines whether or not the user can equip the item. 0 - no; 1 - permanently - 2 only in hands
    # 2 means that its dropped on the ground when unequipped
    canEquip = 0

    def __init__(self, n, t, cq):
        self.name = n
        self.type = t
        self.canEquip = cq

    def recieve(self, ent):
        ent.inventory.append(self)



