#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import pygame

WHITE = (255, 255, 255, 128)

pygame.init()
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Usando lines para pintar el coseno")

pygame.draw.line(surface, WHITE, (0, 200), (600, 200), 1) # El eje
coords = []
for x in range(0, 600, 2):
    y = math.cos(x * math.pi / 180.0)
    coords.append((x, 200 - y*200))

pygame.draw.lines(surface, WHITE, False, coords, 1)

pygame.display.update()
input('Pulsa enter:')
pygame.quit()
