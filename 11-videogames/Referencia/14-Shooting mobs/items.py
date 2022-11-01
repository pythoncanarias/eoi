import pygame
import math
import random
from settings import *
vec = pygame.math.Vector2


class Item (pygame.sprite.Sprite):
    def __init__(self, game, name, x, y):
        self.groups = game.all_sprites, game.items
        self.game = game
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.item_group = game.items
        self.name = name
        self.image = game.images[name]
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.x = x
        self.rect.y = y
        self.pos = vec(x, y)
        self.time_offset = random.uniform(0, 1000)

    def picked_by(self, picker):
        pass
        self.game.fx[self.name].play()

    def update(self):
        self.rect.y = self.pos.y + \
            math.sin(self.time_offset + pygame.time.get_ticks() *
                     ITEM_HOVER_SPEED) * ITEM_HOVER_RANGE


class HealthPack (Item):
    def __init__(self, game, x, y):
        super().__init__(game, 'HEALTH', x, y)

    def picked_by(self, picker):
        super().picked_by(picker)
        heal = ITEMS['HEALTH']['HEAL']
        picker.health = max(0, min(picker.health + heal, picker.max_health))
        self.kill()


class SpeedUp (Item):
    def __init__(self, game, x, y):
        super().__init__(game, 'SPEEDUP', x, y)
        self.picker = None
        self.picked_at = 0
        self.picker_speed = 0
        self.picker_max_speed = 0

    def picked_by(self, picker):
        super().picked_by(picker)
        self.item_group.remove(self)
        self.rect = pygame.Rect(-1000, -1000, 0, 0)
        speed_up = ITEMS['SPEEDUP']['SPEED']
        self.picker = picker
        self.picker_speed = picker.speed
        self.picker_max_speed = picker.max_speed
        picker.speed += speed_up
        picker.max_speed += speed_up
        self.stops_working_at = pygame.time.get_ticks() + \
            ITEMS['SPEEDUP']['DURATION']

    def update(self):
        super().update()
        if self.picker == None:
            return

        now = pygame.time.get_ticks()
        if now > self.stops_working_at:
            self.picker.speed = self.picker_speed
            self.picker.max_speed = self.picker_max_speed
            self.kill()
            print("DONE!")
