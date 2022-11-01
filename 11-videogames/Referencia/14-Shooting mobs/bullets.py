import pygame
import math
import random
from settings import *
vec = pygame.math.Vector2


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x, y, vx, vy, speed, ttl, spread, damage, color, bullet_group):
        """As bullets can be shot by enemies, they need their target group. No enemy fire!"""
        self.groups = game.all_sprites, bullet_group
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((10, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = random.uniform(speed * 0.9, speed * 1.1)
        self.damage = damage
        self.vel = vec(vx + random.uniform(-spread, spread),
                       vy + random.uniform(-spread, spread)).normalize()
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.spawn_time = pygame.time.get_ticks()
        self.ttl = ttl

    def update(self):
        self.pos += self.vel * self.game.dt * self.speed
        self.rect.center = self.pos
        if pygame.sprite.spritecollideany(self, self.game.walls):
            self.kill()
        if pygame.time.get_ticks() - self.spawn_time > self.ttl:
            self.kill()
