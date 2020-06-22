import random
from os import path

from settings import *
from sprites import *


class Map:
    def __init__(self):
        self.entry_point = (0, 0)
        self.map_data = []
        self.map_width = 0
        self.map_height = 0
        self.pixel_width = 0
        self.pixel_height = 0
        pass

    def load_from_file(self, filename):
        """Create a new map_file structure unrelated to map file data...
        Not sure if needed, though!"""
        game_folder = path.dirname(__file__)
        self.map_file_data = []
        with open(path.join(game_folder, "data", filename), 'r') as f:
            for line in f:
                self.map_file_data.append(line)
        self.map_width = len(self.map_file_data[0]) - 1
        self.map_height = len(self.map_file_data)
        self.pixel_width = (self.map_width) * TILESIZE
        self.pixel_height = (self.map_height) * TILESIZE

        for row, rowLine in enumerate(self.map_file_data):
            row_data = []
            for col, colChar in enumerate(rowLine):
                row_data.append(colChar)
            self.map_data.append(row_data)

    def create_sprites_from_data(self, game):
        """Adding interpreter for the Bee mob. 
        It also checks which wall tile typeto place"""
        for row in range(0, self.map_height):
            for col in range(0, self.map_width):
                tile = self.map_data[row][col]
                tile_south = self.map_data[row+1][col] if row + \
                    1 < self.map_height else tile
                if tile == '1':
                    is_wall_top = tile == tile_south
                    Wall(game, col, row, is_wall_top)
                if tile == 'P':
                    self.entry_point = (col, row)
                if tile == 'b':
                    Bee(game, col, row, (game.all_sprites,
                                         game.mobs), game.bee_img, BEE_SPEED)
