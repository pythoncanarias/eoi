import pygame
from settings import *

vec = pygame.math.Vector2


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, height, width)
        self.width = width
        self.height = height
        self.pos = vec(0, 0)

    def apply_to_sprite(self, entity):
        return entity.rect.move(self.camera.topleft)

    def apply_to_pos(self, x, y):
        return (x - self.camera.topleft[0], y - self.camera.topright[1])

    def apply_to_rect(self, rect):
        """Used to move rects to camera space"""
        return pygame.Rect(rect.x - self.camera.topleft[0], rect.y - self.camera.topleft[1], rect.width, rect.height)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - WIDTH), x)
        y = max(-(self.height - HEIGHT), y)
        self.pos = vec(x, y)
        self.camera = pygame.Rect(x, y, self.width, self.height)
