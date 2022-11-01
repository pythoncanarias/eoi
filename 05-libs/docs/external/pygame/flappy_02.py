#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random
import pygame
from pygame.locals import *

WIDTH = 600
HEIGHT = 489
SIZE = (WIDTH, HEIGHT)
CENTER = (WIDTH // 2, HEIGHT // 2)

# Colores
BACKGROUND_COLOR = (13, 213, 223) #71c5cf

FPS = 25

Vel = 0.0
Acc = 0.392 # Metros cada 20 milisegundos al cuadrado
Pos = list(CENTER)

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Trabajando con imágenes ~ Flappy Bird 01')

bird = pygame.image.load('flappy.png')
clock = pygame.time.Clock()

the_end = False
while not the_end:
    for event in pygame.event.get():
        if event.type == QUIT:
            the_end = True
        if event.type == KEYDOWN:
            if event.key in (K_UP, K_SPACE):
                Vel = max(Vel - 9.5, -9.5)

    Vel = Vel + Acc
    Pos[1] = Pos[1] + Vel
    if Pos[1] > HEIGHT:
        the_end = True
    
    screen.fill(BACKGROUND_COLOR)
    screen.blit(bird, Pos)

    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
sys.exit()
