import pygame
from pygame.locals import *
import os


def title():
    pygame.init()

    FPS = 60
    clock = pygame.time.Clock()

    title_screen = pygame.display.set_mode((1200, 800))
    title_img = pygame.image.load(os.path.join(os.getcwd(), 'assets\\backgrounds\\title.png'))
    title_surf = pygame.transform.scale(title_img, (1200, 800)).convert_alpha()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
        title_screen.blit(title_surf, (0, 0))
        pygame.display.update()
        clock.tick(FPS)
