import pygame
import math
from settings import *
from moon import Moon
from sprites import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.start()

    def start(self):
        self.moon = Moon(self, WIDTH, HEIGHT*0.75, 10)
        self.moon.generate_terrain()
        self.player = Player(self, WIDTH//2, 0)

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
        self.player.update(self.moon)

    def draw(self):
        self.screen.fill(DARKGREY)
        self.moon.draw()
        self.player.draw()
        pygame.draw.rect(self.screen, DARKRED, pygame.Rect(5, 5, 200, 25))
        pygame.draw.rect(self.screen, YELLOW, pygame.Rect(
            5, 5, 200*self.player.fuel, 25))
        pygame.display.flip()


game = Game()
game.run()
