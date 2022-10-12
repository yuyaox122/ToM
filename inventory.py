import pygame

pygame.init()
vec = pygame.math.Vector2


class Inventory(pygame.sprite.Sprite):
    def __init__(self, capacity):
        super().__init__()

        self.inventory = {}
        self.equipped = {}
        self.codes = {}
        for i in range(capacity):
            self.inventory[i] = None
        for i in range(3):
            self.equipped[i] = None
        for i in range(3):
            self.codes[i] = None

    def pick_up(self, *args):
        for item in args:
            for i in range(len(self.inventory)):
                if not self.inventory[i]:
                    self.inventory[i] = item
                    break

    def equip(self, *args):
        for item in args:
            for i in range(len(self.equipped)):
                if not self.equipped[i]:
                    self.equipped[i] = item
                    break

    def learn_code(self, *args):
        for item in args:
            for i in range(len(self.codes)):
                if not self.codes[i]:
                    self.codes[i] = item
                    break

    def update(self):
        pass
