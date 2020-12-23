from settings import *
import pygame
import sys
import random
import math


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption(TITLE)

    def run(self):
        self.playing = True
        while self.playing:
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BGCOLOR)
        centerX = WIDTH//2
        centerY = HEIGHT//2
        pygame.draw.circle(self.screen, CAUCASIAN_SKIN,
                           (centerX, centerY), 127, 0)
        pygame.draw.ellipse(self.screen, CAUCASIAN_SKIN,
                            (centerX-150, centerY-16, 300, 200), 0)
        pygame.draw.circle(self.screen, WHITE, (centerX - 64, centerY), 50)
        pygame.draw.circle(self.screen, WHITE, (centerX + 64, centerY), 50)
        pygame.draw.circle(self.screen, BLACK,
                           (centerX - 64 + 16, centerY-8), 16)
        pygame.draw.circle(self.screen, BLACK,
                           (centerX + 64 + 16, centerY-8), 16)
        pygame.draw.arc(self.screen, BLACK,
                        pygame.Rect(WIDTH//2-32, HEIGHT//2+16, 64, 64),
                        math.radians(180), 0, 2)

        flowerX = centerX-64
        flowerY = centerY-127
        pygame.draw.circle(self.screen, WHITE,
                           (flowerX-32, flowerY-32), 32)
        pygame.draw.circle(self.screen, WHITE,
                           (flowerX+32, flowerY-32), 32)
        pygame.draw.circle(self.screen, WHITE,
                           (flowerX+32, flowerY+32), 32)
        pygame.draw.circle(self.screen, WHITE,
                           (flowerX-32, flowerY+32), 32)
        pygame.draw.circle(self.screen, ORANGE, (flowerX, flowerY), 32)

        # pygame.draw.rect(self.screen, GREEN, (64, 64, 64, 128), 1)
        # pygame.draw.line(self.screen, BLUE, (0, HEIGHT), (WIDTH, 0), 5)

        pygame.display.flip()


game = Game()
game.run()
