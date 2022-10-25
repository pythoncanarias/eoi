import pygame
from settings import *
from pygame import Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y, tail_length):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.tail = []
        self.tail_length = tail_length

    def move(self, dx=0, dy=0):
        if len(self.tail) > self.tail_length:
            self.tail.pop()
        self.tail.insert(0, (self.rect.x, self.rect.y))
        self.x += dx
        self.y += dy

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def draw(self, surface):
        for i in range(0, len(self.tail)):
            surface.blit(self.image, (self.tail[i][0], self.tail[i][1]))
