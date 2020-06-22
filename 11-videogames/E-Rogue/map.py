import constants
import pygame
import random


class Tile:
    def __init__(self, block_path):
        self.block_path = block_path


class Map:
    def __init__(self, width, height):
        self.width = constants.MAP_WIDTH
        self.height = constants.MAP_HEIGHT
        self.tiles = [
            [Tile(True) if y == 0 or y == (height-1) or x == 0 or x == (width-1) else Tile(False)
             for y in range(0, height)]
            for x in range(0, width)
        ]
        self.create_cave()

    def create_cave(self):
        start_walls = (int)(self.width * self.height * 0.3)
        for i in range(0, start_walls):
            x = random.randint(1, self.width-1)
            y = random.randint(1, self.height-1)
            if x != y != 5:
                self.tiles[x][y].block_path = True

        iterations = 10
        neighbour_deltas = [(x, y) for x in range(-1, 2)
                            for y in range(-1, 2) if x != 0 or y != 0]
        for j in range(0, iterations):
            tmp_tiles = self.tiles.copy()
            for x in range(1, self.width-1):
                for y in range(1, self.height-1):
                    sum = 0
                    for delta in neighbour_deltas:
                        dx, dy = delta
                        if self.tiles[x+dx][y+dy].block_path:
                            sum = sum + 1
                    if tmp_tiles[x][y].block_path:
                        tmp_tiles[x][y].block_path = sum >= 3
                    else:
                        tmp_tiles[x][y].block_path = sum >= 5
            self.tiles = tmp_tiles.copy()

    def draw(self, surface):
        for x in range(0, constants.MAP_WIDTH):
            for y in range(0, constants.MAP_HEIGHT):
                if self.tiles[x][y].block_path == True:
                    surface.blit(
                        constants.SPRITES.WALL, (x * constants.CELL_WIDTH, y * constants.CELL_HEIGHT))
                else:
                    surface.blit(
                        constants.SPRITES.FLOOR, (x * constants.CELL_WIDTH, y * constants.CELL_HEIGHT))
