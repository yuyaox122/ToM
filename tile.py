import pygame

import random
import os

pygame.init()
vec = pygame.math.Vector2

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RANDOM_COLOUR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# GENERATE BY TOP LEFT CORNER


class WaterTile(pygame.sprite.Sprite):
    def __init__(self, size, pos):
        super().__init__()
        self.img = pygame.image.load(os.path.join(os.getcwd(), 'assets\\tiles\\water.png'))
        self.surf = pygame.transform.scale(self.img, size).convert_alpha()
        self.rect = self.surf.get_rect(topleft=pos)
        self.size = size

        self.Tile = True

        self.overworld_pos = self.rect.topleft

    def move(self):
        pass

    def update(self):
        pass
