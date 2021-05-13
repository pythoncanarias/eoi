#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()
print("Música de Bensound (https://www.bensound.com/)")
pygame.mixer.music.load('bensound-energy.ogg')
pygame.mixer.music.play()
time.sleep(8)
pygame.mixer.music.fadeout(4000)
time.sleep(4)
pygame.quit()
