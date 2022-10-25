#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import pygame
from pygame.locals import *

pygame.init()
tennis_ball_sound = pygame.mixer.Sound('cartoon059.wav')
tennis_ball_sound.set_volume(1.0)
for i in range(3):
    print('.', flush=True, end='')
    time.sleep(1)

print ('Ya!')
tennis_ball_sound.play()
time.sleep(1)
pygame.quit()
