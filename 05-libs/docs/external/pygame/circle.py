#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import QUIT


def main():
    pygame.init()
    surface = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Circulos")
    pygame.draw.circle(surface, (255, 255, 255), (300, 200), 50)
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
