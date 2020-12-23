import pygame
from settings import *
from pygame import Vector2


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.mobs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.topleft = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.desired_velocity = Vector2(0, 0)

    def update(self):
        self.keyboard_input()
        self.move()

    def move(self):
        self.velocity = self.desired_velocity
        next_position = self.rect.center + self.velocity * self.game.dt
        self.rect.centerx = next_position.x
        self.collide_with_walls('horizontal')
        self.rect.centery = next_position.y
        self.collide_with_walls('vertical')

    def collide_with_walls(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.walls, False)
        if len(hits) == 0:
            return
        wall = hits[0]
        if direction == 'horizontal':
            if self.rect.centerx < wall.rect.centerx:
                self.rect.right = wall.rect.left
            else:
                self.rect.left = wall.rect.right
            self.velocity.x = 0
        if direction == 'vertical':
            if self.rect.centery < wall.rect.centery:
                self.rect.bottom = wall.rect.top
            else:
                self.rect.top = wall.rect.bottom
            self.velocity.y = 0

    def keyboard_input(self):
        keystate = pygame.key.get_pressed()

        self.desired_velocity = Vector2(0, 0)
        if keystate[pygame.K_LEFT]:
            self.desired_velocity.x = -PLAYER_SPEED
        if keystate[pygame.K_RIGHT]:
            self.desired_velocity.x = PLAYER_SPEED
        if keystate[pygame.K_UP]:
            self.desired_velocity.y = -PLAYER_SPEED
        if keystate[pygame.K_DOWN]:
            self.desired_velocity.y = PLAYER_SPEED
