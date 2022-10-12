import pygame

import random
import os
from text import Box, Text

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


class NPC(pygame.sprite.Sprite):
    def __init__(self, visible, player, narrator, text, **kwargs):
        super().__init__()
        if visible:
            self.img = pygame.image.load(os.path.join(os.getcwd(), 'assets\\sprites\\npc\\npc.png'))
            self.surf = self.img.convert_alpha()
            self.rect = self.surf.get_rect(topleft=kwargs['pos'])
            self.size = kwargs['size']
            self.overworld_pos = self.rect.topleft
        self.player = player
        self.narrator = narrator
        self.msg = text

        self.text = Text('assets\\sprites\\dialogue\\alphabet.png')

        self.screen = pygame.display.get_surface()

        self.speaking = False

        self.box = Box()

    def dialogue(self):
        self.speaking = not self.speaking

    def move(self):
        pass

    def update(self):
        self.narrator.display_text(self.msg)
        if self.speaking:
            self.narrator.active = True
        else:
            self.narrator.active = False
