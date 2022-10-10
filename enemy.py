import random
import os
import numpy as np

import pygame

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

colours = [RED, BLUE, YELLOW, MAGENTA, CYAN]

# GENERATE BY TOP LEFT CORNER


class Enemy(pygame.sprite.Sprite):
    def __init__(self, size, pos, colour, player, walls, screen, despawn_box):
        super().__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill(colour)
        self.rect = self.surf.get_rect(topleft=pos)

        self.player = player
        self.walls = walls
        self.screen = screen
        self.speed = random.randint(100, 200)/100
        self.direction = vec(0, 0)

        self.overworld_pos = self.rect.topleft
        self.colour = colour

        self.despawn_box = 700

        self.attack = None
        self.defence = None
        self.max_hearts = None
        self.hearts = None
        self.exp = None
        self.type = None

        self.stats = {
            'attack': None,
            'defence': None,
            'max_hearts': None,
            'hearts': None,
            'exp': None,
            'type': None
        }

    def move(self):
        pass
        # put the AI for the enemy here; make it move towards the player
        # maybe add a vector for the player's position? (syntax: vec(x, y))
        # in the player's class of course

    def update(self):
        self.overworld_pos = self.rect.topleft

        if self.rect.right <= self.player.rect.centerx - self.despawn_box\
                or self.rect.left >= self.player.rect.centerx + self.despawn_box\
                or self.rect.bottom <= self.player.rect.centery - self.despawn_box\
                or self.rect.top >= self.player.rect.centery + self.despawn_box:
            self.kill()

        wall_collisions = pygame.sprite.spritecollide(self, self.walls, False)
        if wall_collisions:
            self.kill()


class Healthbar(pygame.sprite.Sprite):
    def __init__(self, screen, enemy):
        super().__init__()
        self.screen = screen
        self.enemy = enemy
        self.health_bar_rect = pygame.Rect(0, 0, self.enemy.hearts*1195/self.enemy.max_hearts, 50)
        self.border_rect = pygame.Rect(0, 0, self.enemy.max_hearts*1195/self.enemy.max_hearts, 50)

    def update(self):
        self.health_bar_rect = pygame.Rect(0, 0, self.enemy.hearts*1195/self.enemy.max_hearts, 50)
        pygame.draw.rect(self.screen, (59, 2, 2), self.border_rect)
        pygame.draw.rect(self.screen, GREEN, self.health_bar_rect)


class ColourSquare(Enemy):
    def __init__(self, pos, player, walls, colour, screen, despawn_box):
        super().__init__((30, 30), pos, colour, player, walls, screen, despawn_box)

        self.attack = 5
        self.defence = 5
        self.max_hearts = 20
        self.hearts = self.max_hearts
        self.exp = 10
        self.type = 'ColourSquare'

        self.stats = {
            'attack': 5,
            'defence': 5,
            'max_hearts': 20,
            'hearts': 20,
            'exp': 10,
            'type': 'ColourSquare'
        }


class AngryStapmone(Enemy):
    def __init__(self, pos, player, walls, colour, screen, despawn_box):
        super().__init__((30, 30), pos, colour, player, walls, screen, despawn_box)

        self.attack = 5
        self.defence = 5
        self.max_hearts = 20
        self.hearts = self.max_hearts
        self.exp = 10
        self.type = 'AngryStapmone'
        self.message = 'STAPMONE staps you in your tracks!'

        self.img = pygame.image.load(os.path.join(os.getcwd(), 'assets\\sprites\\enemy\\angry_stapmone.png'))
        self.surf = pygame.transform.scale(self.img, (40, 40)).convert_alpha()
        self.rect = self.surf.get_rect(topleft=pos)

        self.stats = {
            'attack': 5,
            'defence': 5,
            'max_hearts': 20,
            'hearts': 20,
            'exp': 10,
            'type': 'AngryStapmone'
        }
