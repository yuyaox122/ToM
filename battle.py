import pygame
from pygame.locals import *

from button import Button, ItemButton, FightButton, Selector
from enemy import Healthbar
from text import Text

import os


def battle(player, enemy, inventory):
    pygame.init()
    pygame.font.init()

    vec = pygame.math.Vector2

    text = Text('assets\\sprites\\dialogue\\alphabet.png')

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    HEIGHT = 800
    WIDTH = 1195
    FPS = 60

    clock = pygame.time.Clock()

    battle_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tales of Mapstonia')
    background_colour = BLACK

    item_button = ItemButton((100, 500), inventory)
    fight_button = FightButton((800, 500), inventory)

    buttons = [item_button, fight_button]

    enemy.surf = pygame.transform.scale(enemy.surf, (300, 300))
    enemy.rect = enemy.surf.get_rect(center=(598, 250))

    healthbar = Healthbar(battle_screen, enemy)

    running = True
    enemy_dead = False

    selector = Selector(item_button, buttons)
    selector.pos = vec(20, 450)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if item_button.rect.collidepoint(pos):
                    item_button.activate()
                elif fight_button.rect.collidepoint(pos):
                    for button in buttons:
                        button.pressed = False
                    fight_button.activate()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    enemy.kill()
                    running = False
                    return running

                if event.key == pygame.K_RIGHT:
                    if selector.pos.x < 400:
                        selector.current = selector.options[(selector.options.index(selector.current) + 1)
                                                            % len(selector.options)]
                        selector.pos.x += 580
                if event.key == pygame.K_LEFT:
                    if selector.pos.x >= 400:
                        selector.current = selector.options[(selector.options.index(selector.current) - 1)
                                                            % len(selector.options)]
                        selector.pos.x -= 580
                if event.key == pygame.K_DOWN:
                    if selector.pos.y < 495:
                        selector.current = selector.options[(selector.options.index(selector.current) + 2)
                                                            % len(selector.options)]
                        selector.pos.y += 145
                if event.key == pygame.K_UP:
                    if selector.pos.y >= 495:
                        selector.current = selector.options[(selector.options.index(selector.current) - 2)
                                                            % len(selector.options)]
                        selector.pos.y -= 145
                if event.key == pygame.K_RETURN:
                    if selector.current.__class__.__bases__[0].__name__ == 'Button':
                        if selector.current.__class__.__name__ == "FightButton":
                            for button in buttons:
                                button.pressed = False
                        selector.current.activate()
                    elif selector.current == 'back':
                        for button in buttons:
                            button.pressed = False
                        selector = Selector(item_button, [item_button, fight_button])
                        selector.pos = vec(20, 450)
                    elif selector.current.__class__.__name__ == 'Weapon':
                        enemy.hearts -= selector.current.attributes['damage']

        battle_screen.fill(background_colour)

        selector.rect.topleft = selector.pos

        if enemy.hearts <= 0:
            enemy.kill()
            player.exp += 10
            enemy_dead = True
            running = False

        if player.hearts <= 0:
            enemy_dead = False
            running = False

        battle_screen.blit(enemy.surf, enemy.rect)

        for button in buttons:
            battle_screen.blit(button.surf, button.rect)
        if item_button.pressed:
            battle_screen.blit(item_button.text_surface, (0, 600))
        if fight_button.pressed:
            battle_screen.blit(fight_button.dialogue, (20, 450))
            for i in range(len(inventory.equipped)):
                item_name = inventory.equipped[i].attributes['tag']
                text.show_sentence(item_name,
                                   vec(
                                       (580 - (len(item_name) * 24 + (len(item_name) - 1) * 4)) / 2 + 20 if i % 2 == 0
                                       else (1780 - (len(item_name) * 24 + (len(item_name) - 1) * 4)) / 2 + 20,
                                       648 if i == 2 else 510
                                   ), battle_screen)
            text.show_sentence('BACK', vec((1780 - (4 * 24 + (4 - 1) * 4)) / 2 + 20, 648), battle_screen)
            selector = fight_button.selector

        battle_screen.blit(selector.surf, selector.rect)

        healthbar.update()

        pygame.display.update()
        clock.tick(FPS)

    return enemy_dead
