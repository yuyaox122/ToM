import os

import pygame
from text import Text
from item import Item

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


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, name):
        super().__init__()
        img = pygame.image.load(os.path.join(os.getcwd(), f'assets\\sprites\\battle\\{name}.png'))
        self.surf = pygame.transform.scale(img, (200, 80)).convert_alpha()
        self.rect = self.surf.get_rect(topleft=pos)

        self.display_surf = pygame.display.get_surface()
        self.selector = None

        self.pressed = False


class ItemButton(Button):
    def __init__(self, pos, inventory):
        super().__init__(pos, 'item')

        self.inventory = inventory

        self.text_surface = None

    def activate(self):
        if self.pressed:
            self.pressed = False
        elif not self.pressed:
            self.pressed = True
            font = pygame.font.SysFont('Comic Sans MS', 18)
            self.text_surface = font.render(f'{self.inventory.inventory}', False, WHITE)


class FightButton(Button):
    def __init__(self, pos, inventory):
        super().__init__(pos, 'fight')
        self.dialogue = pygame.image.load(os.path.join(os.getcwd(), f'assets\\sprites\\battle\\dialogue.png'))
        self.dialogue = pygame.transform.scale(self.dialogue, (1160, 290)).convert_alpha()

        self.inventory = inventory

    def activate(self):
        self.pressed = True
        self.selector = Selector(self.inventory.equipped[0], [*list(self.inventory.equipped.values()), 'back'])
        self.selector.pos = vec(20, 450)


class Selector(pygame.sprite.Sprite):
    def __init__(self, first, options):
        super().__init__()
        self.current = first
        self.options = options
        img = pygame.image.load(os.path.join(os.getcwd(), f'assets\\sprites\\battle\\selector.png'))
        self.surf = pygame.transform.scale(img, (580, 145)).convert_alpha()
        self.rect = self.surf.get_rect(bottomright=(0, 0))

        self.pos = None
