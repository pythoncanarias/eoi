import pygame
from settings import *


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, height, width)
        self.width = width
        self.height = height

    def apply_to_sprite(self, entity):
        """Method used to translate sprites in relation to camera"""
        return entity.rect.move(self.camera.topleft)

    def apply_to_pos(self, x, y):
        """Method used to translate positions in relation to camera's"""
        return (x - self.camera.topleft[0], y - self.camera.topright[1])

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - WIDTH), x)
        y = max(-(self.height - HEIGHT), y)
        self.camera = pygame.Rect(x, y, self.width, self.height)
