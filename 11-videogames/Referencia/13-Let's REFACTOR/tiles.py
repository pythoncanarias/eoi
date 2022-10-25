import pygame
import math
import random
from settings import *
vec = pygame.math.Vector2


class Tile (pygame.sprite.Sprite):
    def __init__(self, game, name, x, y, is_wall_top):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.name = name
        self.image = game.tiles[f"{name}_TOP"] if is_wall_top else game.tiles[f"{name}_FRONT"]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
