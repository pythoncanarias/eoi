import pygame
from settings import *
import random
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.force = 0.3
        self.fuel = 1
        self.fuel_consumption = 0.005
        self.alive = True
        self.r = 0

    def update(self, moon):
        if self.alive == False:
            return

        if self.fuel > 0:
            self.keyboard_input()
        self.vy += 0.1
        self.vx *= 0.9
        self.x += self.vx
        self.y += self.vy

        if self.y > moon.get_height_at(self.x):
            self.alive = False

    def keyboard_input(self):
        keystate = pygame.key.get_pressed()
        dx = 0
        dy = 0
        if keystate[pygame.K_LEFT]:
            dx = -self.force
            self.fuel -= self.fuel_consumption
        if keystate[pygame.K_RIGHT]:
            dx = self.force
            self.fuel -= self.fuel_consumption
        if keystate[pygame.K_UP]:
            dy -= self.force
            self.fuel -= self.fuel_consumption

        if abs(self.vx) < 5:
            self.vx += dx
        if abs(self.vy) < 0.5:
            self.vy += dy

        self.vy += dy

    def check_collision(self):
        self.alive = false

    def draw(self):        
        if self.alive == False and self.r < 50:
            pygame.draw.circle(self.game.screen, RED,
                               (self.x, self.y), self.r)
            self.r += 5
        else:
            self.game.screen.blit(self.image, (self.x, self.y-self.rect.height))
