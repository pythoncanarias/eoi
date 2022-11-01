import random
import pygame
from pygame.locals import QUIT

WIDTH = 600
HEIGHT = 400
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def main():
    pygame.init()
    pygame.display.set_caption("Circulos")
    screen = pygame.display.set_mode((600, 400))
    screen.fill(BLACK)
    for _ in range(10):
        x = random.randrange(WIDTH)
        y = random.randrange(HEIGHT)
        r = random.randrange(25, 75)
        pygame.draw.circle(screen, RED, (x, y), r, 0)
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
