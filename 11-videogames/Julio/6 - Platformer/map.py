from sprites import *
from os import path
from pygame import Vector2


class Map:
    def __init__(self):
        self.map_data = []
        self.player_entry_point = Vector2(0, 0)

    def load_from_file(self, filename):
        game_folder = path.dirname(__file__)
        data_folder = path.join(game_folder, 'data')
        with open(path.join(data_folder, filename), 'r') as file:
            for line in file:
                self.map_data.append(line)

    def create_sprites_from_map_data(self, game):
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(game, col, row)
                if tile == '2':
                    Sand(game, col, row)
                if tile == 'P':
                    self.player_entry_point = Vector2(col, row)
