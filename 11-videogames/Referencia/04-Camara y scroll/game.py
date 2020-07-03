import pygame
import sys

from settings import *
from sprites import *
from map import Map
from camera import Camera


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        pass

    def reset(self):
        """Let's load a bigger map and prepare the camera"""
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
            self.dt = self.clock.tick(FPS)/1000
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
        """Drawing is more tricky now, because we have to apply the camera's rect to 
        sprites and points and everthing's position"""
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
