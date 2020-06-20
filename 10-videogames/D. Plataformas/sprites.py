import pygame
from settings import *
from pygame.math import Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        """Player position is not a cell in the map but a point in game space.
        Player class will also handle input, and resolve collisions against map walls"""
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.vx, self.vy = 0, 0  # Used to store input.
        self.trigger_jump = False
        self.grounded = False
        self.velocity = Vector2(0, 0)

        self.last_keys = None

    def update(self):
        """Get desired velocity from input, then resolve collisions with walls, one coordinate at a time"""
        self.handle_input()

        self.velocity += Vector2(self.vx, self.vy) * self.game.dt
        self.velocity.y += GRAVITY * self.game.dt

        if self.trigger_jump:
            self.velocity.y -= PLAYER_JUMP_FORCE
            self.trigger_jump = False
            self.grounded = False

        self.x += self.velocity.x * self.game.dt
        self.y += self.velocity.y * self.game.dt

        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')

        self.velocity *= 0.9

    def handle_input(self):
        """Reset, register and store desired player direction"""
        self.vx = self.vy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vx = -PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vx = PLAYER_SPEED
        if keys[pygame.K_SPACE] and self.last_keys != None and self.last_keys[pygame.K_SPACE] == False:
            if self.grounded:
                self.trigger_jump = True

        if keys[pygame.K_ESCAPE]:
            self.game.quit()

        self.last_keys = keys

    def collide_with_walls(self, dir):
        """Use pygame.sprite's spritecollide method to find collisions. 
        Then solve collisions by pushing the sprite out of the offending hit."""
        hits = pygame.sprite.spritecollide(self, self.game.walls, False)

        if len(hits) == 0:
            return

        if dir == 'x':
            if self.velocity.x > 0:
                self.x = hits[0].rect.left - self.rect.width
            if self.velocity.x < 0:
                self.x = hits[0].rect.right
            self.velocity.x = 0
            self.rect.x = self.x

        if dir == 'y':
            if self.velocity.y > 0:
                self.y = hits[0].rect.top - self.rect.height
            if self.velocity.y < 0:
                self.y = hits[0].rect.bottom
            self.velocity.y = 0
            self.rect.y = self.y
            self.grounded = True


class Wall (pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
