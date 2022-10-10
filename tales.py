import random

import pygame
import numpy as np
# from pygame.locals import *

from title import title
from battle import battle
from enemy import ColourSquare, AngryStapmone
from inventory import Inventory
from item import Item, Weapon
from player import Player, UI
from wall import Wall
from world_gen import World
from camera import CameraGroup
from npc import NPC
from text import Narrator

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

HEIGHT = 800
WIDTH = 1200
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tales of Mapstonia')
clock = pygame.time.Clock()

background_colour = WHITE
ui_visible = True

ENEMY_SPAWN_BOX = 800
ENEMY_DESPAWN_BOX = 1000

SCROLLING = True

walls = pygame.sprite.Group()
enemies = pygame.sprite.Group()
npc_group = pygame.sprite.Group()
# implementing camera
if SCROLLING:
    all_sprites = CameraGroup(screen)
else:
    all_sprites = pygame.sprite.Group()

inventory = Inventory(10)
MOUSE_CURSOR = Weapon({'tag': 'MOUSE CURSOR', 'damage': 5}, inventory)
KEYBOARD = Weapon({'tag': 'KEYBOARD', 'damage': 10}, inventory)
REWRITE_CODE = Weapon({'tag': 'REWRITE CODE', 'damage': 100}, inventory)

inventory.pick_up(MOUSE_CURSOR, KEYBOARD, REWRITE_CODE)
for i in range(len(inventory.equipped)):
    inventory.equip(inventory.inventory[i])

item = Item({'tag': 'a square'}, inventory)
items = pygame.sprite.Group()
items.add(item)

player = Player((400, 400), walls, enemies, npc_group)
ui = UI(screen, player)

narrator = Narrator(player)
# box = Box()

Joe = NPC(True, player, narrator, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                                  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                                  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', **{'size': (30, 30), 'pos': (300, 300)})
npc_group.add(Joe)

NUMBER_OF_ENEMIES = 5

for _ in range(NUMBER_OF_ENEMIES):
    stapmone = AngryStapmone(
        (player.rect.left + random.randint(-ENEMY_SPAWN_BOX, ENEMY_SPAWN_BOX),
         player.rect.top + random.randint(-ENEMY_SPAWN_BOX, ENEMY_SPAWN_BOX)),
        player, walls, random.choice(colours), screen, ENEMY_DESPAWN_BOX)
    enemies.add(stapmone)
    all_sprites.add(stapmone)


if __name__ == "__main__":
    title()
    world = World(walls, all_sprites)
    for i in range(20):
        world.change_tile((i, 0), 1)
        world.change_tile((i, 19), 1)
        world.change_tile((0, i), 1)
        world.change_tile((19, i), 1)
    world.initialise_tiles()

    all_sprites.add(player)
    all_sprites.add(item)
    all_sprites.add(Joe)

    narrator.active = True

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_BACKSPACE:
                    player.hearts -= 1

                if event.key == pygame.K_TAB:
                    player.exp += random.randint(1, 10)
                    player.exp = player.exp % player.max_exp

                if event.key == pygame.K_SPACE:
                    if narrator.active:
                        narrator.active = False

                    player_item_collisions = pygame.sprite.spritecollide(player, items, False)
                    for item in player_item_collisions:
                        item.picked_up()
                    for npc in npc_group:
                        if abs(npc.rect.centerx - player.rect.centerx) <=\
                                (player.surf.get_width() + npc.surf.get_width())/2\
                                and abs(npc.rect.centery - player.rect.centery) <= \
                                (player.surf.get_height() + npc.surf.get_width())/2:
                                    npc.dialogue()
                                                        
                if event.key == pygame.K_h:
                    for _ in range(100):
                        stapmone = AngryStapmone(                    
                            (player.rect.left + random.randint(-ENEMY_SPAWN_BOX, ENEMY_SPAWN_BOX),
                             player.rect.top + random.randint(-ENEMY_SPAWN_BOX, ENEMY_SPAWN_BOX)),
                            player, walls, random.choice(colours), screen, ENEMY_DESPAWN_BOX)
                        enemies.add(stapmone)
                        all_sprites.add(stapmone)

        player_enemy_collisions = pygame.sprite.spritecollide(player, enemies, False)
        if player_enemy_collisions:
            current_enemy = player_enemy_collisions[0]
            running = battle(player, current_enemy, inventory)

        screen.fill(background_colour)

        # drawing all the sprites
        if SCROLLING:
            all_sprites.custom_draw_sprite(player)
        else:
            for sprite in all_sprites:
                screen.blit(sprite.surf, sprite.rect)
        all_sprites.update()

        if ui_visible:
            ui.display(player.exp, player.max_exp)

        if len(enemies) <= NUMBER_OF_ENEMIES:
            for _ in range(NUMBER_OF_ENEMIES - len(enemies)):
                stapmone = AngryStapmone(
                    (player.rect.left + random.randint(-ENEMY_SPAWN_BOX, ENEMY_SPAWN_BOX),
                     player.rect.top + random.randint(-ENEMY_SPAWN_BOX, ENEMY_SPAWN_BOX)),
                    player, walls, random.choice(colours), screen, ENEMY_DESPAWN_BOX)
                enemies.add(stapmone)
                all_sprites.add(stapmone)

        pygame.display.update()
        clock.tick(FPS)
