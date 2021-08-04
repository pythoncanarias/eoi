#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import pygame

WHITE = (255, 255, 255, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Antialiasing")

pygame.draw.ellipse(surface, WHITE, (100, 100, 400, 200)) 
pygame.draw.arc(surface, RED, (50, 50, 500, 300), 0, math.pi/2, 2) 
pygame.draw.arc(surface, BLUE, (50, 50, 500, 300), math.pi, 3 * math.pi / 2, 2) 

pygame.display.update()
input('Pulsa enter:')
pygame.quit()
