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
BACKGROUND_COLOR = (13, 213, 223) 
RED = (110, 26, 26)

FPS = 25

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Trabajando con Texto 01')

font = pygame.font.Font('badaboom.ttf', 72)
texto = font.render("Badaboom", True, RED)
 
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)
    screen.blit(texto, CENTER)
    clock.tick(FPS)
    pygame.display.update()

