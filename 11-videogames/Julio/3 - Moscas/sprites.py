import pygame
from settings import *
import random


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.move()
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def move(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)
        if self.x > GRIDWIDTH:
            self.x = 0
        if self.x < 0:
            self.x = GRIDWIDTH-1
        if self.y > GRIDHEIGHT:
            self.y = 0
        if self.y < 0:
            self.y = GRIDHEIGHT-1
