import pygame

import random
import os
import math

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


class Box:
    def __init__(self):
        self.surf = pygame.Surface((1120, 280), pygame.SRCALPHA)
        self.img = pygame.transform.scale(
            pygame.image.load(os.path.join(os.getcwd(), 'assets\\sprites\\dialogue\\text_box.png')),
            (1120, 280)
        )
        # self.img = pygame.image.load(os.path.join(os.getcwd(), 'assets\\sprites\\dialogue\\text_box.png'))
        self.rect = self.surf.get_rect()

        self.screen = pygame.display.get_surface()
        self.npc_text_present = False
        self.dialogue_text_present = True

        self.text_speed = 1
        self.i = 0
        self.offset = 0

    def move(self):
        pass

    def update(self):
        self.surf.blit(self.img, (0, 0))

    def show_sentence(self, text, message, pos):  # shows the sentence in the box
        for j in range(math.floor(self.i)+1):
            order = list(enumerate(message))[j][0]
            index = order % 35
            if index == 0 and order != 0:
                pos.y += 42
                self.surf.blit(text.get_letter(message[j]), vec(70, pos.y))
            else:
                if message[j] != message[0] and message[j-1] == '!':
                    self.surf.blit(text.get_letter(message[j]), vec(pos.x+index*28-16, pos.y))
                else:
                    self.surf.blit(text.get_letter(message[j]), vec(pos.x+index*28, pos.y))
        if self.i < len(message) - self.text_speed:
            self.i += self.text_speed

    def update_message_box(self, text, message, screen, player):
        screen.blit(self.surf, (40, 500))
        self.update()
        self.show_sentence(text, message, vec(70, 50))


class Text:
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.screen = pygame.display.get_surface()

    def image_at(self, rectangle, **kwargs):
        rect = pygame.Rect(rectangle)  # format of (topleft_x, topleft_y, x_change, y_change)
        image = pygame.Surface(rect.size, pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), rect)
        if kwargs:
            if kwargs['char'] == '!':
                image = pygame.transform.scale(image, (8, 32))
        else:
            image = pygame.transform.scale(image, (24, 32))
        return image

    def get_letter(self, letter):
        letter = letter.upper()
        letters = {'A': (0, 0),
                   'B': (7, 0),
                   'C': (14, 0),
                   'D': (21, 0),
                   'E': (28, 0),
                   'F': (0, 9),
                   'G': (7, 9),
                   'H': (14, 9),
                   'I': (21, 9),
                   'J': (28, 9),
                   'K': (0, 18),
                   'L': (7, 18),
                   'M': (14, 18),
                   'N': (21, 18),
                   'O': (28, 18),
                   'P': (0, 27),
                   'Q': (7, 27),
                   'R': (14, 27),
                   'S': (21, 27),
                   'T': (28, 27),
                   'U': (0, 36),
                   'V': (7, 36),
                   'W': (14, 36),
                   'X': (21, 36),
                   'Y': (28, 36),
                   'Z': (0, 45),
                   '!': (7, 45),
                   '?': (10, 45),
                   ' ': (17, 45)
                   }

        if letter == '!':
            return self.image_at((letters[letter][0], letters[letter][1], 2, 8), **{'char': '!'})
        else:
            return self.image_at((letters[letter][0], letters[letter][1], 6, 8))

    def show_sentence(self, message, pos, surf):  # shows the sentence on the screen
        for (index, letter) in enumerate(message):
            surf.blit(self.get_letter(letter), (pos.x+index*28, pos.y))


class Narrator:
    def __init__(self, player):
        self.text = Text('assets\\sprites\\dialogue\\alphabet.png')
        self.box = Box()
        self.screen = pygame.display.get_surface()
        self.player = player

        self.active = False

    def display_text(self, msg):
        if self.active:
            self.box.update_message_box(self.text, msg, self.screen, self.player)
            self.player.speed = 0
        elif not self.active:
            self.player.speed = self.player.stats['speed']
            self.box.i = 0

