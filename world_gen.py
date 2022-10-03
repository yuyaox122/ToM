import pygame

from wall import Wall, Boulder
from worlds import world_list
from tile import WaterTile

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

TILE_SIZE = 40


class World:
    def __init__(self, walls, all_sprites):
        super().__init__()

        self.world_tiles = world_list['blank']
        self.walls = walls
        self.all_sprites = all_sprites

    def create_tile(self, pos, name):
        if name == 1:
            wall = Wall((TILE_SIZE, TILE_SIZE), (TILE_SIZE*pos.x, TILE_SIZE*pos.y))
            self.walls.add(wall)
            self.all_sprites.add(wall)

        elif name == 2:
            tile = WaterTile((TILE_SIZE, TILE_SIZE), (TILE_SIZE*pos.x, TILE_SIZE*pos.y))
            self.all_sprites.add(tile)

        elif name == 3:
            wall = Boulder((TILE_SIZE, TILE_SIZE), (TILE_SIZE*pos.x, TILE_SIZE*pos.y))
            self.walls.add(wall)
            self.all_sprites.add(wall)

    def initialise_tiles(self):
        for row in list(enumerate(self.world_tiles)):
            for tile in list(enumerate(row[1])):
                self.create_tile(vec(tile[0], row[0]), tile[1])

    def change_tile(self, pos, tile_type):
        self.world_tiles[pos[1]][pos[0]] = tile_type
