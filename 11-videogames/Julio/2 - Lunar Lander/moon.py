import pygame
from settings import *
import random


class Moon():
    def __init__(self, game, width, max_height, min_height):
        self.game = game
        self.width = width
        self.min_height = min_height
        self.max_height = max_height
        self.mid_height = (min_height+max_height)/2
        self.heights = []

    def generate_terrain(self, ):
        h = random.randrange(self.min_height, self.max_height)
        landing_spot_x = random.randrange(self.width*0.2, self.width*0.8)
        landing_spot_width = 25
        go_up = h < self.mid_height
        accumulated = 0
        for i in range(0, self.width):
            if go_up:
                h += random.uniform(0, 5)
            else:
                h -= random.uniform(0, 5)
            accumulated = random.uniform(0, 0.1)
            h = max(self.min_height, min(self.max_height, h))
            if random.random() < accumulated or h == self.mid_height or h == self.max_height:
                go_up = not go_up
                accumulated = 0
            self.heights.append(h)

        landing_spot_height = self.heights[landing_spot_x]
        for i in range(landing_spot_x-landing_spot_width, landing_spot_x+landing_spot_width):
            self.heights[i] = landing_spot_height

    def draw(self):
        for i in range(0, len(self.heights)):
            pygame.draw.line(self.game.screen, ORANGE,
                             (i, HEIGHT), (i, HEIGHT-self.heights[i]), 1)

    def get_height_at(self, x):
        return HEIGHT-self.heights[int(x)]
