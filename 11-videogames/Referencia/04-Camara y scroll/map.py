import random
from os import path

from settings import *
from sprites import Wall


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
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, filename), 'r') as f:
            for line in f:
                self.map_data.append(line)
        self.map_width = len(self.map_data[0]) - 1
        self.map_height = len(self.map_data)
        self.pixel_width = (self.map_width) * TILESIZE
        self.pixel_height = (self.map_height) * TILESIZE

    def create_sprites_from_data(self, game):
        for row, tiles in enumerate(self.map_data):
            for col, tiles in enumerate(tiles):
                if tiles == '1':
                    Wall(game, col, row)
                if tiles == 'P':
                    self.entry_point = (col, row)
