import pygame
from settings import *
import random
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.tail_image = pygame.Surface((TILESIZE, TILESIZE))
        self.tail_image.fill(DARKYELLOW)
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.speed = 10
        self.turn = 0
        self.tail = []
        self.tail_length = 1
        self.alive = True

    def grow(self):
        self.tail_length += 1
        self.speed += 0.1

    def update(self):
        self.move()
        self.wrap_around_world()
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def move(self):
        self.turn += self.speed * self.game.dt

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] and self.dx == 0:
            self.dx = -1
            self.dy = 0
        if keystate[pygame.K_RIGHT] and self.dx == 0:
            self.dx = 1
            self.dy = 0
        if keystate[pygame.K_UP] and self.dy == 0:
            self.dx = 0
            self.dy = -1
        if keystate[pygame.K_DOWN] and self.dy == 0:
            self.dx = 0
            self.dy = 1

        if (self.turn >= 1):
            self.turn = 0
            self.update_tail()
            self.x += self.dx
            self.y += self.dy
            self.check_death()

    def wrap_around_world(self):
        if self.x >= GRIDWIDTH:
            self.x = 0
        if self.x < 0:
            self.x = GRIDWIDTH-1
        if self.y >= GRIDHEIGHT:
            self.y = 0
        if self.y < 0:
            self.y = GRIDHEIGHT-1

    def update_tail(self):
        if len(self.tail) >= self.tail_length:
            self.tail.pop()
        self.tail.insert(0, (self.x, self.y))

    def draw_tail(self, surface):
        for i in range(0, len(self.tail)):
            x = self.tail[i][0] * TILESIZE
            y = self.tail[i][1] * TILESIZE
            surface.blit(self.tail_image, (x, y))

    def check_death(self):
        is_stopped = self.dx == 0 and self.dy == 0
        if is_stopped == False and (self.x, self.y) in self.tail:
            self.alive = False
            print("OUCH!")


class Fruit(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.fruits
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.teleport()

    def teleport(self):
        x = random.randint(0, GRIDWIDTH-1)
        y = random.randint(0, GRIDHEIGHT-1)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
