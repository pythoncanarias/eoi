import pygame
import math
from random import uniform
from settings import *
vec = pygame.math.Vector2


class Mob (pygame.sprite.Sprite):
    def __init__(self, game, x, y, groups, image, speed, health):
        """Mobs now have health and register external forces"""
        self.groups = groups
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.forces = vec(0, 0)
        self.speed = speed
        self.pos = vec(x, y) * TILESIZE
        self.health = health
        self.max_health = health

    def move(self):
        """Position is updated with desired velocity and external forces,
        and forces are reduced on each frame"""
        self.pos += self.vel * (self.speed * self.game.dt) + self.forces
        self.forces *= 0.95
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')

    def hit(self, damage):
        """A mob that is hit reduces its health, and eventually dies"""
        self.health -= damage
        if self.health < 0:
            self.kill()

    def attack(self, target):
        """A mob attacks by reducing target's health. This WILL change"""
        target.health -= 5
        self.push(target)

    def push(self, target):
        """Pushing a mob updates its external forces vector.
        This requires future tweaks..."""
        target.forces = target.forces + (target.pos - self.pos) * BEE_KNOCKBACK

    def collide_with_walls(self, dir):
        """Using rect centers instead of top-left corners. This is confusing in pygame"""
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
        """Mob's health is shown as a bar drawn in relation to mob's sprite"""
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
        """Add health"""
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
        """Adds health"""
        super().__init__(game, x, y, groups, game.bee_img, speed, health)

    def update(self):
        """Defensive programming here, normalization fails if magnitude is 0"""
        towards_player = self.game.player.pos - self.pos
        if towards_player.magnitude() != 0:
            self.vel = towards_player.normalize()
            self.move()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x, y, vx, vy, speed, ttl, spread, damage, color):
        """Different bullets may inflict different damage"""
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
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.top_wall_img if is_wall_top else game.front_wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
