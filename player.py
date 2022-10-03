import os

import pygame
from pygame.locals import *

pygame.init()
vec = pygame.math.Vector2

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

HEIGHT = 800
WIDTH = 800


# GENERATE BY TOP LEFT CORNER


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, walls, enemies, npc):
        super().__init__()
        self.img = pygame.image.load(os.path.join(os.getcwd(), 'assets\\sprites\\player\\stap.png'))
        # self.img = pygame.transform.scale(self.img, (self.img.get_width()*1.5, self.img.get_height()*1.5))
        self.surf = self.img.convert_alpha()
        self.rect = self.surf.get_rect(topleft=pos)

        self.walls = walls
        self.enemies = enemies
        self.npc = npc

        self.speed = 5
        self.direction = vec(0, 0)

        self.hearts = 3
        self.max_hearts = 3
        self.exp = 0
        self.max_exp = 100
        self.attack = 1
        self.defence = 0
        self.level = 1

        self.stats = {
            'hearts': self.hearts,
            'max_hearts': self.max_hearts,
            'exp': self.exp,
            'max_exp': self.max_exp,
            'attack': self.attack,
            'defence': self.defence,
            'level': self.level,
            'speed': self.speed,
        }

        self.inventory = {}
        for i in range(10):
            self.inventory[i] = None

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.direction.x = -1
        elif pressed_keys[K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        if pressed_keys[K_UP]:
            self.direction.y = -1
        elif pressed_keys[K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

    def collision_x(self):
        wall_collisions = pygame.sprite.spritecollide(self, self.walls, False)
        npc_collisions = pygame.sprite.spritecollide(self, self.npc, False)
        for w in wall_collisions:
            if w.rect.colliderect(self.rect):
                if self.direction.x > 0:
                    self.rect.right = w.rect.left
                if self.direction.x < 0:
                    self.rect.left = w.rect.right

        for w in npc_collisions:
            if w.rect.colliderect(self.rect):
                if self.direction.x > 0:
                    self.rect.right = w.rect.left
                if self.direction.x < 0:
                    self.rect.left = w.rect.right

    def collision_y(self):
        wall_collisions = pygame.sprite.spritecollide(self, self.walls, False)
        npc_collisions = pygame.sprite.spritecollide(self, self.npc, False)
        for w in wall_collisions:
            if w.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = w.rect.top
                if self.direction.y < 0:
                    self.rect.top = w.rect.bottom

        for w in npc_collisions:
            if w.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = w.rect.top
                if self.direction.y < 0:
                    self.rect.top = w.rect.bottom

    def death(self):
        self.hearts = self.max_hearts
        self.exp = 0
        self.rect.topleft = (100, 100)

    def update(self):
        if self.hearts <= 0:
            self.death()
        self.rect.x += self.direction.x * self.speed
        self.collision_x()
        self.rect.y += self.direction.y * self.speed
        self.collision_y()
        self.move()
        # self.stats = {
        #     'hearts': self.hearts,
        #     'max_hearts': self.max_hearts,
        #     'exp': self.exp,
        #     'max_exp': self.max_exp,
        #     'attack': self.attack,
        #
        #     'defence': self.defence,
        #     'level': self.level
        # }


class UI:
    def __init__(self, screen, player):
        self.exp_bar_rect = pygame.Rect(10, 10, 200, 20)
        self.health_bar_rect = pygame.Rect(10, 34, 200, 20)
        self.border_colour = (34, 34, 34)
        self.exp_colour = (80, 174, 236)
        self.hearts = pygame.image.load(os.path.join(os.getcwd(), 'assets\\sprites\\player\\heart.png'))

        self.screen = screen
        self.player = player

    def display(self, current, max_amount):
        ratio = current / max_amount
        current_rect = self.exp_bar_rect.copy()
        current_rect.width = current_rect.width * ratio
        pygame.draw.rect(self.screen, self.border_colour, self.exp_bar_rect)
        pygame.draw.rect(self.screen, self.exp_colour, current_rect)
        pygame.draw.rect(self.screen, BLACK, self.exp_bar_rect, 3)

        heart = pygame.transform.scale(self.hearts, (50, 50)).convert_alpha()
        heart_row = 34
        heart_x = 10
        for x in range(self.player.hearts):
            if heart_x + 50 > WIDTH:
                heart_x = 10
                heart_row += 70
            self.screen.blit(heart, (heart_x, heart_row))
            heart_x += 60

    def update(self):
        pass
