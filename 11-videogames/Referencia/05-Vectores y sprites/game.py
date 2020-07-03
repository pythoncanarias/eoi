#
# ART:  https://kenney.nl/assets/platformer-art-pixel-redux
#

import pygame
import sys
from os import path

from settings import *
from sprites import *
# Use the spritesheet class to simplify sprite location
from spritesheet import Spritesheet
from map import Map
from camera import Camera


class Game:
    def __init__(self):
        pygame.init()
        # Using fullsize will make the game take the whole screen
        self.screen = pygame.display.set_mode(
            [WIDTH, HEIGHT])  # pygame.FULLSCREEN | pygame.DOUBLEBUF
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        """Load a spritesheet from file, use it to define game sprites"""
        root_folder = path.dirname(__file__)

        sprites = Spritesheet(
            path.join(root_folder, "data", "img", "spritesheet.png"))
        self.player_img = sprites.image_at(28, 0, TILESIZE, 1, (94, 129, 162))
        pass

    def reset(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        self.current_map = Map()
        self.current_map.load_from_file("bigMap.txt")
        self.current_map.create_sprites_from_data(self)

        self.player = Player(
            self, self.current_map.entry_point[0], self.current_map.entry_point[1])

        self.camera = Camera(self.current_map.pixel_width,
                             self.current_map.pixel_height)

    def run(self):
        self.playing = True
        while self.playing:
            # Let's remove the division and just user natural ticks
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

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        """Let's show frames per second here"""
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
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
