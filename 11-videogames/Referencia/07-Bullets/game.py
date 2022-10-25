#
# ART:  https://kenney.nl/assets/platformer-art-pixel-redux
#

import pygame
import sys
from os import path

from settings import *
from sprites import *
from spritesheet import Spritesheet
from map import Map
from camera import Camera


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            [WIDTH, HEIGHT])  # pygame.FULLSCREEN | pygame.DOUBLEBUF
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        root_folder = path.dirname(__file__)

        sprites = Spritesheet(
            path.join(root_folder, "data", "img", "spritesheet.png"))

        self.player_img = sprites.image_at(
            PLAYER_SPRITE_AT[0], PLAYER_SPRITE_AT[1], TILESIZE, 1, KEY)

        self.bee_img = sprites.image_at(
            BEE_SPRITE_AT[0], BEE_SPRITE_AT[1], TILESIZE, 1, KEY)

        self.top_wall_img = sprites.image_at(
            TOP_WALL_SPRITE_AT[0], TOP_WALL_SPRITE_AT[1], TILESIZE, 1, KEY)
        self.front_wall_img = sprites.image_at(
            FRONT_WALL_SPRITE_AT[0], FRONT_WALL_SPRITE_AT[1], TILESIZE, 1, KEY)

    def reset(self):
        """Let's add a bullets group"""
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.current_map = Map()
        self.current_map.load_from_file("bigMap.txt")
        self.current_map.create_sprites_from_data(self)

        self.player = Player(
            self,
            self.current_map.entry_point[0], self.current_map.entry_point[1],
            self.all_sprites,
            self.player_img,
            PLAYER_SPEED)

        self.camera = Camera(self.current_map.pixel_width,
                             self.current_map.pixel_height)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw(self):
        """Updated camera apply method to use sprites or positions"""
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(DARKGREY)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply_to_sprite(sprite))

        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

    def show_start_screen(self):
        pass


game = Game()
game.show_start_screen()

while True:
    game.reset()
    game.run()
