import pygame
import math
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        pass

    def draw(self):
        # Utilizando line, circle, rect y arc, dibujar una cara

        # rect(surface, color, rect) -> Rect  Rect(left, top, width, height)
        # circle(surface, color, center, radius)
        # line(surface, color, start_pos, end_pos, width)
        # arc(surface, color, rect, start_angle, stop_angle)

        pygame.draw.circle(self.screen, PINK, (WIDTH // 2, HEIGHT // 2), 128)
        pygame.draw.circle(self.screen, BLACK, (250, 200), 10)
        pygame.draw.circle(self.screen, BLACK, (390, 200), 10)
        pygame.draw.arc(self.screen, BLACK, pygame.Rect(
            270, 200, 100, 50), math.radians(180), 0, 3)

        # Nothing else to draw, let's show it!
        pygame.display.flip()


game = Game()
game.run()
