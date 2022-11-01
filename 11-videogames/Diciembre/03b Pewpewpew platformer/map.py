from os import path
from sprites import Wall, Wasp, Wasp_Nest, HealthPack, WeaponCrate
from pygame import Vector2
from settings import *


class Map:
    def __init__(self):
        self.map_data = []
        self.entry_point = Vector2(0, 0)

    def load_map_from_file(self, filename):
        root_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(root_folder, "assets", filename), 'r') as file:
            for line in file:
                self.map_data.append(line)

    def create_sprites_from_data(self, game):
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                pixel_x = col*TILESIZE
                pixel_y = row*TILESIZE
                if tile == '1':
                    Wall(game, col, row)
                if tile == 'P':
                    self.entry_point = Vector2(pixel_x, pixel_y)
                if tile == 'w':
                    Wasp(game, pixel_x, pixel_y)
                if tile == 'W':
                    Wasp_Nest(game, pixel_x, pixel_y)
                if tile == 'h':
                    HealthPack(game, pixel_x, pixel_y)
                if tile == 'c':
                    WeaponCrate(game, pixel_x, pixel_y)
