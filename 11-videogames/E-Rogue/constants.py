import pygame
from os import path

SPRITE_SIZE = 16

GAME_WIDTH = 800
GAME_HEIGHT = 600
CELL_WIDTH = 16
CELL_HEIGHT = 16

MAP_WIDTH = 30
MAP_HEIGHT = 30

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY = (100, 100, 100)

COLOR_DEFAULT_BG = COLOR_BLACK

SPRITES = None


class Sprites:
    def __init__(self):
        root_folder = path.dirname(__file__)
        # Images
        img_folder = path.join(root_folder, "data", "tiles")

        self.PLAYER = pygame.image.load(
            path.join(img_folder, "tile025.png")).convert_alpha()
        self.CREATURE = pygame.image.load(
            path.join(img_folder, "tile123.png")).convert_alpha()
        self.WALL = pygame.image.load(
            path.join(img_folder, "tile016.png")).convert_alpha()
        self.FLOOR = pygame.image.load(
            path.join(img_folder, "tile000.png")).convert_alpha()
