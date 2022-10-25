import pygame
import math
from random import uniform
from settings import *
vec = pygame.math.Vector2


class Mob (pygame.sprite.Sprite):
    def __init__(self, game, x, y, groups, image, speed, health):
        """Removed TILESIZE, x, y must be pixel coordinates now. Set rect here for things that don't move"""
        self.groups = groups
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.forces = vec(0, 0)
        self.speed = speed
        self.pos = vec(x, y)
        self.rect.x, self.rect.y = self.pos.x, self.pos.y
        self.health = health
        self.max_health = health

    def move(self):
        self.pos += self.vel * (self.speed * self.game.dt) + self.forces
        self.forces *= 0.95
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')

    def hit(self, damage):
        self.health -= damage
        if self.health < 0:
            self.kill()

    def attack(self, target):
        target.health -= 5
        self.push(target)

    def push(self, target):
        target.forces = target.forces + (target.pos - self.pos) * BEE_KNOCKBACK

    def collide_with_walls(self, dir):
        hits = pygame.sprite.spritecollide(self, self.game.walls, False)

        if len(hits) == 0:
            return

        if dir == 'x':
            if hits[0].rect.centerx > self.rect.centerx:
                self.pos.x = hits[0].rect.left - self.rect.width
            if hits[0].rect.centerx < self.rect.centerx:
                self.pos.x = hits[0].rect.right
            self.vel.x = 0
            self.rect.x = self.pos.x

        if dir == 'y':
            if hits[0].rect.centery > self.rect.centery:
                self.pos.y = hits[0].rect.top - self.rect.height
            if hits[0].rect.centery < self.rect.centery:
                self.pos.y = hits[0].rect.bottom
            self.vel.y = 0
            self.rect.y = self.pos.y

    def draw_health(self):
        surface = self.game.screen
        health = self.health / self.max_health
        if health > 0.6:
            col = GREEN
        elif health > 0.3:
            col = YELLOW
        else:
            col = RED
        width = int(self.rect.width * health)
        p = self.pos + self.game.camera.pos

        self.health_bar = pygame.Rect(p.x, p.y, width, 7)
        if self.health < self.max_health:
            pygame.draw.rect(surface, col, self.health_bar)


class Player (Mob):
    def __init__(self, game, x, y, groups, image, speed, health):
        super().__init__(game, x, y, groups, image, speed, health)
        self.last_shot_time = -1000

    def update(self):
        self.handle_input()
        self.move()
        if self.health < 0:
            self.kill()

    def handle_input(self):
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
                   BASIC_GUN_SPEED, BASIC_GUN_TTL, BASIC_GUN_SPREAD, BASIC_GUN_DAMAGE,  BASIC_GUN_COLOR)


class Bee (Mob):
    def __init__(self, game, x, y, groups, image, speed, health):
        super().__init__(game, x, y, groups, game.bee_img, speed, health)

    def update(self):
        towards_player = self.game.player.pos - self.pos
        if towards_player.magnitude() != 0:
            self.vel = towards_player.normalize()
            self.move()


class BeeNest (Mob):
    """Here's a new kind of mob: nests. They can be killed too, but
    they are able to spawn other creatures"""

    def __init__(self, game, x, y, groups, image, health, spawn_frequency, max_population):
        super().__init__(game, x, y, groups, game.bee_img, 0, health)
        # TODO would be nice to have a group of my own spawned critters
        self.spawn_frequency = spawn_frequency
        self.last_spawn_time = 0
        self.spawn_group = pygame.sprite.Group()
        self.max_population = max_population

    def update(self):
        is_max_population_reached = len(
            self.spawn_group) == self.max_population
        frequency_reached = pygame.time.get_ticks(
        ) - self.last_spawn_time > self.spawn_frequency

        if is_max_population_reached == False and frequency_reached:
            Bee(self.game, self.pos.x, self.pos.y, (self.game.all_sprites, self.game.mobs, self.spawn_group),
                self.game.bee_img, BEE_SPEED, BEE_HEALTH)
            self.last_spawn_time = pygame.time.get_ticks()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x, y, vx, vy, speed, ttl, spread, damage, color):
        self.groups = game.all_sprites, game.bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((10, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.damage = damage
        self.vel = vec(vx + uniform(-spread, spread),
                       vy + uniform(-spread, spread)).normalize()
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


class Wall (pygame.sprite.Sprite):
    def __init__(self, game, x, y, is_wall_top):
        """Same as mobs, x, y are pixel positions now"""
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.top_wall_img if is_wall_top else game.front_wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
