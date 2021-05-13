#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random
import pygame
from pygame.locals import *

WIDTH = 600
HEIGHT = 489
SIZE = (WIDTH, HEIGHT)

FPS = 60

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Campo de estrellas 3')

estrellas = []
for i in range(60):
    estrella = [
        random.randrange(0, WIDTH+1),
        random.randrange(0, HEIGHT+1),
        random.random() * 3.0,
        ]
    estrellas.append(estrella)

WHITE = (255,255,255)
SILVER = (128,128,128)
BLACK = (0, 0, 0)

movimiento = [0.0, 0.0]
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                movimiento[0] -= 1
            elif event.key == K_RIGHT:
                movimiento[0] += 1
            elif event.key == K_UP:
                movimiento[1] -= 1
            elif event.key == K_DOWN:
                movimiento[1] += 1
            elif event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Update starts
    for estrella in estrellas:
        velocidad = estrella[2]
        estrella[0] = estrella[0]+(movimiento[0] * velocidad)
        estrella[1] = estrella[1]+(movimiento[1] * velocidad)
        if estrella[0] < 0:
            estrella[0] += WIDTH
        elif estrella[0] > WIDTH:
            estrella[0] -= WIDTH
        if estrella[1] < 0:
            estrella[1] += HEIGHT
        elif estrella[1] > HEIGHT:
            estrella[1] -= HEIGHT


    screen.fill(BLACK)
    for estrella in estrellas:
        (x, y, vel) = estrella
        x = int(round(x))
        y = int(round(y))
        pygame.draw.circle(screen, WHITE, (x, y), 2)
        
    pygame.display.flip()
    pygame.display.update()
    clock.tick(FPS)

