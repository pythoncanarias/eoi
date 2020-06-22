import pygame
# Let's add Math and Random, it will be handy
import math
from random import uniform
from settings import *
vec = pygame.math.Vector2


class Mob (pygame.sprite.Sprite):
    def __init__(self, game, x, y, groups, image, speed):
        self.groups = groups
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.speed = speed
        self.pos = vec(x, y) * TILESIZE

    def move(self):
        self.pos += self.vel * (self.speed * self.game.dt)
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')

    def collide_with_walls(self, dir):
        hits = pygame.sprite.spritecollide(self, self.game.walls, False)

        if len(hits) == 0:
            return

        if dir == 'x':
            if self.vel.x > 0:
                self.pos.x = hits[0].rect.left - self.rect.width
            if self.vel.x < 0:
                self.pos.x = hits[0].rect.right
            self.vel.x = 0
            self.rect.x = self.pos.x

        if dir == 'y':
            if self.vel.y > 0:
                self.pos.y = hits[0].rect.top - self.rect.height
            if self.vel.y < 0:
                self.pos.y = hits[0].rect.bottom
            self.vel.y = 0
            self.rect.y = self.pos.y


class Player (Mob):
    def __init__(self, game, x, y, groups, image, speed):
        """Player is able to shoot, so it will control shooting frequency.
        NOT GOOD. Weapong are certainly a class of their own, but this will
        do for now"""
        super().__init__(game, x, y, groups, image, speed)
        self.last_shot_time = -1000

    def update(self):
        self.handle_input()
        self.move()

    def handle_input(self):
        """And mouse input to target and shoot, creating Bullets"""
        self.vel = vec(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel.x = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel.x = 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vel.y = -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vel.y = 1
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071

        if keys[pygame.K_ESCAPE]:
            self.game.quit()

        mouse = pygame.mouse.get_pressed()
        if mouse[0] and pygame.time.get_ticks() - self.last_shot_time > BASIC_GUN_FIRING_RATE:
            x, y = pygame.mouse.get_pos()
            camera_fix = self.game.camera.apply_to_pos(x, y)
            bullet_velocity = (
                vec(camera_fix[0], camera_fix[1]) - self.pos).normalize()
            self.last_shot_time = pygame.time.get_ticks()

            Bullet(self.game, self.rect.center[0], self.rect.center[1], bullet_velocity.x, bullet_velocity.y,
                   BASIC_GUN_SPEED, BASIC_GUN_TTL, BASIC_GUN_SPREAD, BASIC_GUN_COLOR)


class Bee (Mob):
    def __init__(self, game, x, y, groups, image, speed):
        super().__init__(game, x, y, groups, game.bee_img, speed)

    def update(self):
        towards_player = self.game.player.pos - self.pos
        self.vel = towards_player.normalize()
        self.move()


class Bullet(pygame.sprite.Sprite):
    """Bullets are entities of their own, quite simple for now:
    They will just follow a trajectory until their TTL expires"""

    def __init__(self, game, x, y, vx, vy, speed, ttl, spread, color):
        self.groups = game.all_sprites, game.bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((10, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.vel = vec(vx + uniform(-spread, spread),
                       vy + uniform(-spread, spread)).normalize()
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.spawn_time = pygame.time.get_ticks()
        self.ttl = ttl

    def update(self):
        """Similar to Mobs, but bullets are killed if they collide with
        something or if their TTL expires"""
        self.pos += self.vel * self.game.dt * self.speed
        self.rect.center = self.pos
        if pygame.sprite.spritecollideany(self, self.game.walls):
            self.kill()
        if pygame.time.get_ticks() - self.spawn_time > self.ttl:
            self.kill()
        # Just a test: mimic mob killing by just destroying their sprite
        bee_hit_list = pygame.sprite.spritecollide(
            self, self.game.mobs, True)


class Wall (pygame.sprite.Sprite):
    def __init__(self, game, x, y, is_wall_top):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.top_wall_img if is_wall_top else game.front_wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
