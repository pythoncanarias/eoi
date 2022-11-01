import pygame
from settings import *


class Camera:
    """Cameras in pygame are somewhat a hack. We define their with and height (usually the map size), the point
    they must track (player's position, for instance), we update their position to keep that point centered, and then
    use it's rect to DRAW EVERYTHING ELSE. 
    We'll basically translate everything using the camera's rect."""

    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, height, width)
        self.width = width
        self.height = height

    def apply(self, entity):
        """Traslate an entity so its position is relative to the camera's"""
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        """Keep the camera's target centered"""
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - WIDTH), x)
        y = max(-(self.height - HEIGHT), y)
        self.camera = pygame.Rect(x, y, self.width, self.height)
