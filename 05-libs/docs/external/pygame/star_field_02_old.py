#!/usr/bin/env python

import random
import pygame
from pygame.locals import *

estrellas = []
for i in range(10):
    estrella = (
        random.randrange(0, 601),
        random.randrange(0, 481)
        )
    estrellas.append(estrella)

pygame.init()
screen = pygame.display.set_mode((600, 480))
pygame.display.set_caption('Campo de estrellas')
clock = pygame.time.Clock()

FPS = 15

WHITE = (255,255,255)
BLACK = (0,0,0)

while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update starts
    for i, estrella in enumerate(estrellas[:]):
        x, y = estrella
        if x <= 300:
            x -= 1
        else:
            x += 1
        if y <= 240:
            y -= 1
        else:
            y += 1
        estrellas[i] = (x,y)


    for estrella in estrellas:
        pygame.draw.circle(screen, WHITE, estrella, 2, 0)
    
    pygame.display.update()
    clock.tick(FPS)
