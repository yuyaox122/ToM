import random

import pygame

pygame.init()
vec = pygame.math.Vector2


class Item(pygame.sprite.Sprite):
    def __init__(self, attributes, inventory):
        super().__init__()
        self.attributes = attributes
        self.inventory = inventory

        self.is_item = True

        self.surf = pygame.Surface((20, 20))
        self.surf.fill((20, 120, 30))
        self.rect = self.surf.get_rect(topleft=(random.randint(100, 500), random.randint(100, 500)))

        self.overworld_pos = self.rect.topleft

    def picked_up(self):
        if not self.inventory.inventory[len(self.inventory.inventory) - 1]:
            self.inventory.pick_up(self)
            self.kill()

    def update(self):
        pass


class Weapon(Item):
    def __init__(self, attributes, inventory):
        super().__init__(attributes, inventory)

