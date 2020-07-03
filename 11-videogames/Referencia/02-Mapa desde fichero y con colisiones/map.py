import random
from os import path

from sprites import Wall


class Map:
    def __init__(self):
        """Nothing fancy yet: just the player entry point and an array of text lines that represent the map"""
        self.entry_point = (0, 0)
        self.map_data = []
        pass

    def load_from_file(self, filename):
        """Load a map from a text file"""
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'r') as f:
            for line in f:
                self.map_data.append(line)

    def create_sprites_from_data(self, game):
        """Create wall sprites from map data and register player entry point"""
        for row, tiles in enumerate(self.map_data):
            for col, tiles in enumerate(tiles):
                if tiles == '1':
                    Wall(game, col, row)
                if tiles == 'P':
                    self.entry_point = (col, row)
