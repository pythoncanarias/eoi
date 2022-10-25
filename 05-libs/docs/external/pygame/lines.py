#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

WHITE = (255, 255, 255, 128)

pygame.init()
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Líneas")
for y in range(10, 101, 10):
    pygame.draw.line(surface, WHITE, (10, y), (100, y), 1)
for x in range(10, 101, 10):
    pygame.draw.line(surface, WHITE, (x, 10), (x, 100), 1)

pygame.display.flip()
input('Pulsa enter:')
pygame.quit()
