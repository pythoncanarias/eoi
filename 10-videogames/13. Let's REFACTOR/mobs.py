import pygame
import math
import random
from settings import *
from items import *
from bullets import *
vec = pygame.math.Vector2


class Mob (pygame.sprite.Sprite):
    def __init__(self, game, name, x, y, groups, image, speed, health):
        """Added current velocity to use inertia and an avoidance vector"""
        self.groups = groups
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.velocity = self.vel
        self.forces = vec(0, 0)
        self.avoidance = vec(0, 0)
        self.speed = speed
        self.pos = vec(x, y)
        self.rect.x, self.rect.y = self.pos.x, self.pos.y
        self.health = health
        self.max_health = health
        self.max_speed = MAX_SPEED

    def move(self):
        """Adding some lerping to smooth movement up! Including avoidance vector"""
        self.velocity = self.velocity.lerp(self.vel * self.speed +
                                           self.forces + self.avoidance, MOBS[self.name]['ACCELERATION'])

        if self.velocity.magnitude() > self.max_speed:
            self.velocity = self.velocity.normalize() * self.max_speed

        self.forces *= 0.9
        self.avoidance *= 0.9
        self.pos = self.pos + self.velocity
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
        towards_target = (target.pos - self.pos)
        if towards_target.magnitude() > 0:
            target.forces = target.forces + \
                (target.pos - self.pos).normalize() * \
                MOBS[self.name]['KNOCKBACK']

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

    def avoid_mobs(self):
        """Compute avoidance vector to steer away from other mobs"""
        for mob in self.game.mobs:
            if mob != self:
                towards_mov = mob.pos - self.pos
                if 0.1 < towards_mov.magnitude() < AVOID_RADIUS:
                    self.avoidance -= towards_mov.normalize() / (towards_mov.magnitude() / AVOID_RADIUS)


class Player (Mob):
    def __init__(self, game, x, y, groups, image, speed, health):
        """HO! HO! HO! Now I have a SHOTGUN"""
        super().__init__(game, 'PLAYER', x, y, groups, image, speed, health)
        self.last_shot_time = -1000
        self.weapon_name = 'GUN'

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

        # Moving shooting to its own function
        if mouse[0]:
            self.shoot()

    def shoot(self):
        # Shooting now depends on current weapon
        weapon = WEAPONS[self.weapon_name]

        if pygame.time.get_ticks() - self.last_shot_time < weapon['FIRING_RATE']:
            return

        x, y = pygame.mouse.get_pos()
        camera_fix = self.game.camera.apply_to_pos(x, y)
        bullet_velocity = (
            vec(camera_fix[0], camera_fix[1]) - self.pos).normalize()
        self.last_shot_time = pygame.time.get_ticks()

        self.game.fx[self.weapon_name].play()
        for _ in range(0, weapon['AMMO_PER_SHOT']):
            Bullet(self.game, self.rect.center[0], self.rect.center[1], bullet_velocity.x, bullet_velocity.y,
                   weapon['SPEED'],
                   weapon['TTL'],
                   weapon['SPREAD'],
                   weapon['DAMAGE'],
                   weapon['COLOR']
                   )


class Bee (Mob):
    def __init__(self, game, name, x, y, groups, image, speed, health):
        """Adding some variance to base stats"""
        speed = random.uniform(speed * 0.9, speed * 1.1)
        health = random.uniform(health * 0.9, health * 1.1)
        super().__init__(game, name, x, y, groups, image, speed, health)

    def update(self):
        """Update avoid vector! and some crude patrolling"""
        towards_player = self.game.player.pos - self.pos
        self.avoid_mobs()
        if 0 < towards_player.magnitude() < MOBS[self.name]['VISION_RADIUS']:
            self.vel = towards_player.normalize()
        else:
            if random.uniform(1, 100) < 10:
                self.vel = vec(random.uniform(-1, 1), random.uniform(-1, 1))
        self.move()


class BeeNest (Mob):
    def __init__(self, game, name, x, y, groups, image, health, spawn_frequency, max_population):
        super().__init__(game, name, x, y, groups, image, 0, health)
        self.spawn_frequency = spawn_frequency
        self.last_spawn_time = 0
        self.spawn_group = pygame.sprite.Group()
        self.max_population = max_population

    def update(self):
        """Spawn more than one creature at a time"""
        spawnables = self.max_population - len(self.spawn_group)
        frequency_reached = pygame.time.get_ticks(
        ) - self.last_spawn_time > self.spawn_frequency

        if spawnables > 0 and frequency_reached:
            for _ in range(1, random.randint(1, spawnables)):
                offset = self.pos + vec(random.uniform(-25, 25),
                                        random.uniform(-25, 25))
                Bee(self.game, 'BEE', offset.x, offset.y, (self.game.all_sprites, self.game.mobs, self.spawn_group),
                    self.game.images['BEE'], MOBS['BEE']['SPEED'], MOBS['BEE']['HEALTH'])
            self.last_spawn_time = pygame.time.get_ticks()
