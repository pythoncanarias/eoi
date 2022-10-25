#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

pygame.init()
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Circulos")
pygame.draw.circle(surface, (255, 255, 255), (300, 200), 50)
pygame.display.flip()
input('Pulsa enter:')
pygame.quit()
