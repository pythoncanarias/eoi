#!/usr/bin/env python

import sys
import random
import pygame
from pygame.locals import QUIT

WIDTH = 600
HEIGHT = 489
SIZE = (WIDTH, HEIGHT)

WHITE = (255,255,255)
BLACK = (0, 0, 0)

FPS = 25

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Campo de estrellas 1')

estrellas = []
for i in range(50):
    estrella = [
        random.randrange(0, WIDTH+1),
        random.randrange(0, HEIGHT+1)
        ]
    estrellas.append(estrella)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update starts
    for estrella in estrellas:
        estrella[0] = estrella[0]-1
        if estrella[0] < 0:
            estrella[0] += WIDTH

    # dibujar_y_refrescar_pantalla
    screen.fill(BLACK)
    for estrella in estrellas:
        pygame.draw.circle(screen, WHITE, estrella, 2, 1)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
