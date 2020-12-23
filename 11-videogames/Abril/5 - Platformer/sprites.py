import pygame
from settings import *
from pygame import Vector2
import math


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.rect.x, self.rect.y = x * TILESIZE, y * TILESIZE


class Player(pygame.sprite.Sprite):
    def __init__(self, game, position):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.position = position * TILESIZE
        self.desired_velocity = Vector2(0, 0)
        self.velocity = Vector2(0, 0)
        self.grounded = False
        self.trigger_jump = False
        self.jump_time = 0

    def update(self):
        self.handle_input()

        self.velocity.x -= self.velocity.x * DRAG * self.game.dt
        self.velocity += (Vector2(0, GRAVITY) +
                          self.desired_velocity * PLAYER_ACCELERATION) * self.game.dt
        if self.trigger_jump:
            self.trigger_jump = False
            self.velocity.y = PLAYER_JUMP_SPEED * 0.5
            self.jump_time += self.game.dt

        if abs(self.velocity.y) > PLAYER_MAX_Y_SPEED:
            self.velocity.y = math.copysign(
                PLAYER_MAX_Y_SPEED, self.velocity.y)

        self.position += self.velocity * self.game.dt

        self.rect.x = self.position.x
        self.collide_with_walls('x')
        self.rect.y = self.position.y
        self.collide_with_walls('y')

    def handle_input(self):
        vx, vy = 0, 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            vx = -1
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            vx = 1
        if key[pygame.K_UP] or key[pygame.K_w]:
            if self.grounded or self.jump_time < PLAYER_JUMP_TIME:
                self.trigger_jump = True
        else:
            self.jump_time = PLAYER_JUMP_TIME

        self.desired_velocity = Vector2(vx, vy)
        if self.desired_velocity.magnitude() > 0:
            self.desired_velocity = self.desired_velocity.normalize()

    def collide_with_walls(self, dir):
        hits = pygame.sprite.spritecollide(self, self.game.walls, False)
        if len(hits) == 0:
            self.grounded = False
            return

        if dir == 'x':
            if self.velocity.x > 0:
                self.position.x = hits[0].rect.left - self.rect.width
            if self.velocity.x < 0:
                self.position.x = hits[0].rect.right
            self.velocity.x = 0
            self.rect.x = self.position.x

        if dir == 'y':
            if self.velocity.y > 0:
                self.position.y = hits[0].rect.top - self.rect.height
                self.grounded = True
                self.jump_time = 0

            if self.velocity.y < 0:
                self.position.y = hits[0].rect.bottom
            self.velocity.y = 0
            self.rect.y = self.position.y
