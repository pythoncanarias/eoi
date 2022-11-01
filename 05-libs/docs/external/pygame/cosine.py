#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import pygame
from pygame.locals import QUIT

WHITE = (255, 255, 255, 128)


def main():
    pygame.init()
    surface = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Usando lines para pintar el coseno")

    pygame.draw.line(surface, WHITE, (0, 200), (600, 200), 1)  # El eje
    coords = []
    for x in range(0, 600, 2):
        y = math.cos(x * math.pi / 180.0)
        coords.append((x, 200 - y*200))

    pygame.draw.lines(surface, WHITE, False, coords, 1)

    in_game = True
    while in_game:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                in_game = False
                break
    pygame.quit()


if __name__ == "__main__":
    main()
