import pygame

from settings import *
vec = pygame.math.Vector2


class Mob (pygame.sprite.Sprite):
    """Base mob class that will handle most of the things that any
    mob can do - and we'll consider player a mob. Move, Hit, Die...
    We are creating this from Player, which is just different because
    of how it controls movement."""

    def __init__(self, game, x, y, groups, image, speed):
        """Init now takes the mob image and base speed"""
        self.groups = groups
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.speed = speed
        self.pos = vec(x, y) * TILESIZE

    def move(self):
        """Moving is now a base method for all things moving.
        At least for all those that are solid and collide with walls!"""
        self.pos += self.speed * self.vel * self.game.dt
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
    """Player is just another mob, but its desired velocity is set
    by the player using an input method (keyboard/mouse)"""

    def __init__(self, game, x, y, groups, image, speed):
        super().__init__(game, x, y, groups, image, speed)

    def update(self):
        self.handle_input()
        self.move()

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


class Bee (Mob):
    """Our first mob! It has a very basic brain, for now..."""

    def __init__(self, game, x, y, groups, image, speed):
        super().__init__(game, x, y, groups, game.bee_img, speed)

    def update(self):
        """The update method for a mob is its brain. In the player, it's
        the human's through input. In regular mobs, it will depend on 
        what we want the mob to do. Bees will just fly towards
        the player, for now"""
        towards_player = self.game.player.pos - self.pos
        self.vel = towards_player.normalize()
        self.move()


class Wall (pygame.sprite.Sprite):
    def __init__(self, game, x, y, is_wall_top):
        """Use different tiles depending on wall configuration"""
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.top_wall_img if is_wall_top else game.front_wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
