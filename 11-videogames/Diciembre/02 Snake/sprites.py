import pygame
from settings import *
import random


class Snake(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.head_image = pygame.Surface((TILESIZE, TILESIZE))
        self.head_image.fill(YELLOW)
        self.rect = self.head_image.get_rect()
        self.tail_part_image = pygame.Surface((TILESIZE, TILESIZE))
        self.tail_part_image.fill(GREEN)
        self.game = game
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.speed = 10
        self.cooldown = 1
        self.tail = []
        self.tail_length = 5
        self.isAlive = True

    def update(self):
        self.move()
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def draw(self, surface):
        surface.blit(self.head_image, self.rect)
        for part in self.tail:
            screen_x = part[0] * TILESIZE
            screen_y = part[1] * TILESIZE
            surface.blit(self.tail_part_image, (screen_x, screen_y))

    def move(self):
        self.keyboard_input()
        self.cooldown -= self.speed * self.game.dt
        if self.cooldown < 0:
            self.update_tail()
            self.x += self.dx
            self.y += self.dy
            self.cooldown = 1
            self.check_death()

        self.stay_within_world()

    def check_death(self):
        isMoving = self.dx != 0 or self.dy != 0
        head = (self.x, self.y)
        if head in self.tail and isMoving:
            self.isAlive = False

    def grow(self):
        self.tail_length += 1
        self.speed += 1

    def update_tail(self):
        self.tail.insert(0, (self.x, self.y))
        if len(self.tail) >= self.tail_length:
            self.tail.pop()

    def keyboard_input(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] and self.dx == 0:
            self.dx = -1
            self.dy = 0
        if keystate[pygame.K_RIGHT] and self.dx == 0:
            self.dx = 1
            self.dy = 0
        if keystate[pygame.K_UP] and self.dy == 0:
            self.dy = -1
            self.dx = 0
        if keystate[pygame.K_DOWN] and self.dy == 0:
            self.dy = 1
            self.dx = 0

    def stay_within_world(self):
        if self.x > GRIDWIDTH-1:
            self.x = 0
        elif self.x < 0:
            self.x = GRIDWIDTH-1
        if self.y > GRIDHEIGHT-1:
            self.y = 0
        elif self.y < 0:
            self.y = GRIDHEIGHT-1


class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.teleport_to_random_position()

    def teleport_to_random_position(self):
        self.x = random.randint(0, GRIDWIDTH-1)
        self.y = random.randint(0, GRIDHEIGHT-1)
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def draw(self, surface):
        surface.blit(self.image, self.rect)
