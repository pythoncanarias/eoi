#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import pygame
from pygame.locals import QUIT

WHITE = (255, 255, 255, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


def main():
    pygame.init()
    surface = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Círculos y elipsis")
    pygame.draw.ellipse(surface, WHITE, (100, 100, 400, 200))
    pygame.draw.arc(surface, RED, (50, 50, 500, 300), 0, math.pi/2, 2)
    pygame.draw.arc(surface, BLUE, (50, 50, 500, 300), math.pi, 3 * math.pi / 2, 2)
    pygame.draw.circle(surface, (255, 255, 255), (300, 200), 50)

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
