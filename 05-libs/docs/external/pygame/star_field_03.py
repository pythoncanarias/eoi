#!/usr/bin/env python

import sys
import random
import math

import pygame
from pygame.locals import QUIT

FPS = 15

WHITE = (255,255,255)
BLACK = (0,0,0)

WIDTH = 600
HEIGHT = 480
MID_WIDTH = WIDTH // 2
MID_HEIGHT = HEIGHT // 2

estrellas = []
for i in range(300):
    estrella = (
        random.randrange(0, WIDTH+1),
        random.randrange(0, HEIGHT+1)
        )
    estrellas.append(estrella)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Campo de estrellas 3')
clock = pygame.time.Clock()

def move_star(star):
    x, y = star
    delta_x = x - MID_WIDTH
    delta_y = y - MID_HEIGHT
    mo = math.sqrt(delta_x**2 + delta_y**2)
    x += delta_x / mo
    y += delta_y / mo
    return (x,y)


while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update starts
    for i, estrella in enumerate(estrellas[:]):
        x, y = move_star(estrella)
        estrellas[i] = (x,y)

    for estrella in estrellas:
        x = int(round(estrella[0]))
        y = int(round(estrella[1]))
        pygame.draw.circle(screen, WHITE, (x, y), 2, 0)
    
    pygame.display.update()
    clock.tick(FPS)
