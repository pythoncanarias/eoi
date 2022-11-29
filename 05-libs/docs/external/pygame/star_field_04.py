#!/usr/bin/env python

import random
import math

import pygame
from pygame.locals import QUIT

FPS = 15 * 2

WHITE = (255,255,255)
BLACK = (0,0,0)

WIDTH = 600
HEIGHT = 480
MID_WIDTH = WIDTH // 2
QUARTER_WIDTH = WIDTH // 4

MID_HEIGHT = HEIGHT // 2
QUARTER_HEIGHT = HEIGHT // 4

estrellas = []
for i in range(300):
    estrella = (
        random.randrange(0, WIDTH+1),
        random.randrange(0, HEIGHT+1)
        )
    estrellas.append(estrella)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Campo de estrellas 4')
clock = pygame.time.Clock()

def move_star(star):
    global MID_WIDTH, MID_HEIGHT
    x, y = star
    delta_x = x - MID_WIDTH
    delta_y = y - MID_HEIGHT
    mo = math.sqrt(delta_x**2 + delta_y**2)
    x += delta_x / mo
    y += delta_y / mo
    return (x,y)

def is_out_of_screen(estrella):
    global WIDTH, HEIGHT
    x, y = estrella
    return x < 0 or x > WIDTH or y < 0 or y > HEIGHT

def new_star():
    estrella = (
        random.randrange(QUARTER_WIDTH, WIDTH - QUARTER_WIDTH + 1),
        random.randrange(QUARTER_HEIGHT, HEIGHT - QUARTER_HEIGHT + 1)
        )
    return estrella

def get_magnitud(star):
    global MID_WIDTH, MID_HEIGHT
    x, y = star
    delta_x = x - MID_WIDTH
    delta_y = y - MID_HEIGHT
    mo = int(round(math.sqrt(delta_x**2 + delta_y**2)))
    return mo * 4 // 300

    
def main():
    while True:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    
        # Update starts
        for i, estrella in enumerate(estrellas[:]):
            x, y = move_star(estrella)
            estrellas[i] = (x,y)
    
        for estrella in estrellas:
            x = int(round(estrella[0]))
            y = int(round(estrella[1]))
            radio = get_magnitud(estrella)
            pygame.draw.circle(screen, WHITE, (x, y), radio, 0)
        
        pygame.display.update()
    
        # Sustituimos estrella desaparecidas por nuevas
        for i, estrella in enumerate(estrellas[:]):
            if is_out_of_screen(estrella):
                estrellas[i] = new_star()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
