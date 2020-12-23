import pygame
from settings import *
from pygame import Vector2
import random


class Brick(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.bricks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        # self.image.fill(GREEN)
        self.image = random.choice(game.brick_images)
        self.rect = self.image.get_rect()
        self.rect.center = Vector2(x, y)

    def hit(self):
        self.game.break_fx.play()
        self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        #self.image = pygame.Surface((PAD_WIDTH, PAD_HEIGHT))
        # self.image.fill(ORANGE)
        self.image = game.pad_image
        self.rect = self.image.get_rect()
        self.rect.center = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.acceleration = 0

    def update(self):
        self.keyboard_input()
        self.move()

    def move(self):
        self.velocity.x += self.acceleration * self.game.dt
        if self.velocity.magnitude() > PAD_MAX_SPEED:
            self.velocity.scale_to_length(PAD_MAX_SPEED)
        self.rect.centerx += self.velocity.x * self.game.dt

        self.velocity -= Vector2(self.velocity.x * DRAG * self.game.dt, 0)
        if self.velocity.magnitude() < 20:
            self.velocity.x = 0

        if self.rect.centerx < PAD_WIDTH//2:
            self.rect.centerx = PAD_WIDTH//2
            self.velocity.x = 0
        if self.rect.centerx > WIDTH - PAD_WIDTH//2:
            self.rect.centerx = WIDTH - PAD_WIDTH//2
            self.velocity.x = 0

    def hit(self, ball):
        # -ancho/2      0       ancho/2
        # -1                          1
        offset = (ball.rect.centerx - self.rect.centerx) / (self.rect.width//2)
        ball.velocity.x = offset
        ball.rect.bottom = self.rect.top

    def keyboard_input(self):
        keystate = pygame.key.get_pressed()

        self.acceleration = 0
        if keystate[pygame.K_LEFT]:
            self.acceleration = -PAD_ACCELERATION
        if keystate[pygame.K_RIGHT]:
            self.acceleration = PAD_ACCELERATION


class Ball(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.balls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #self.image = pygame.Surface((BALL_RADIUS, BALL_RADIUS))
        # self.image.fill(YELLOW)
        self.image = game.ball_image
        self.rect = self.image.get_rect()
        self.rect.center = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.isAsleep = True
        self.push = 0

    def update(self):
        if self.isAsleep:
            if self.game.player.acceleration != 0 and self.game.player.velocity.magnitude() != 0:
                self.velocity = self.game.player.velocity.normalize() + Vector2(0, -1)
                self.isAsleep = False
            return

        if self.velocity.magnitude() != 0:
            self.rect.center += self.velocity.normalize() * (BALL_SPEED + self.push) * self.game.dt
        self.push *= 0.9

        if self.rect.centerx > WIDTH:
            self.rect.centerx = WIDTH
            self.velocity.x *= -1
            self.push = 500
        if self.rect.centerx < 0:
            self.rect.centerx = 0
            self.velocity.x *= -1
            self.push = 500
        if self.rect.centery < 0:
            self.rect.centery = 0
            self.velocity.y *= -1
            self.push = 500

        if self.rect.centery > HEIGHT:
            self.kill()
            self.game.ball_lost()

    def bounce(self, thing):
        if self.velocity.magnitude() == 0:
            return
        velocity = self.velocity.normalize()

        is_vertical_bounce = velocity.x == 0

        if velocity.x != 0:

            v_slope = -velocity.y / velocity.x

            corner = thing.rect.center
            if v_slope > 0 and velocity.x > 0:  # Q1 bottom left
                corner = thing.rect.bottomleft
            if v_slope < 0 and velocity.x < 0:  # Q2 bottom right
                corner = thing.rect.bottomright
            if v_slope > 0 and velocity.x < 0:  # Q3 top right
                corner = thing.rect.topright
            if v_slope < 0 and velocity.x > 0:  # Q4 top left
                corner = thing.rect.topleft

            towards_thing = (Vector2(corner) -
                             Vector2(self.rect.center))

            if towards_thing.magnitude() == 0:
                return

            towards_thing = towards_thing.normalize()

            if towards_thing.x == 0:
                is_vertical_bounce = True
            else:
                t_slope = towards_thing.y / towards_thing.x
                is_vertical_bounce = abs(v_slope) > abs(t_slope)

        if is_vertical_bounce:
            self.velocity.y *= -1
        else:
            self.velocity.x *= -1

        self.game.bounce_fx.play()
        self.push = 500
