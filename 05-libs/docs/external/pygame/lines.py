#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import QUIT

WHITE = (255, 255, 255, 128)


def main():
    pygame.init()
    surface = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Líneas")
    for y in range(10, 101, 10):
        pygame.draw.line(surface, WHITE, (10, y), (100, y), 1)
    for x in range(10, 101, 10):
        pygame.draw.line(surface, WHITE, (x, 10), (x, 100), 1)
    pygame.display.flip()
    in_game = True
    while in_game:
        for event in pygame.event.get():
            if event.type == QUIT:
                in_game = False
                break
    pygame.quit()


if __name__ == "__main__":
    main()
