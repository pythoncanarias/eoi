#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
import random
import pygame
from pygame.locals import *

WIDTH = 600
HEIGHT = 489
SIZE = (WIDTH, HEIGHT)
CENTER = (WIDTH // 2, HEIGHT // 2)

# Colores
BACKGROUND_COLOR = (13, 213, 223) #71c5cf
RED = (110, 26, 26)
BLACK = (10, 10, 10)

FPS = 25

Vel = 0.0
Acc = 0.392 # Metros cada 20 milisegundos al cuadrado
Pos = list(CENTER)

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Trabajando con imágenes ~ Flappy Bird 03')

bird = pygame.image.load('flappy.png')
clock = pygame.time.Clock()

def wait_for_exit(num_s):
    count = 0
    exit_now = False
    for i in range(num_s*4):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                exit_now = True
        if exit_now:
            break
        time.sleep(0.25)

def show_game_over(sfc):
    font = pygame.font.Font('badaboom.ttf', 72)
    texto = font.render("GAME OVER", True, RED)
    rect = texto.get_rect()
    rect.center = CENTER
    sfc.blit(texto, rect)

    barkentina = pygame.font.Font('barkentina.otf', 24)
    press_any_key_message = barkentina.render('Press any key to exit', True, BLACK)
    rect = press_any_key_message.get_rect()
    rect.centerx = CENTER[0]
    rect.centery = CENTER[1] + 72
    sfc.blit(press_any_key_message, rect)
    pygame.display.update()

the_end = False
while not the_end:
    for event in pygame.event.get():
        if event.type == QUIT:
            the_end = True
        if event.type == KEYDOWN:
            if event.key in (K_UP, K_SPACE):
                Vel = max(Vel - 9.5, -9.5)

    Vel = Vel + Acc
    Pos[1] = Pos[1] + Vel
    if Pos[1] > HEIGHT:
        the_end = True
    
    screen.fill(BACKGROUND_COLOR)
    screen.blit(bird, Pos)

    clock.tick(FPS)
    pygame.display.update()

show_game_over(screen)
wait_for_exit(7)
pygame.quit()
sys.exit()
