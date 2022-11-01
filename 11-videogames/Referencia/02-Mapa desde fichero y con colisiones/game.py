import pygame
import sys

from settings import *
from sprites import *
from map import Map


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
        """Create a new Map object and initialize it. It will also contain
        the start position for our player."""
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        self.current_map = Map()
        self.current_map.load_from_file("map.txt")
        self.current_map.create_sprites_from_data(self)

        self.player = Player(
            self, self.current_map.entry_point[0], self.current_map.entry_point[1])

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

    def draw(self):
        """Map will also be drawn because wall sprites belong
        to the all_sprites group"""
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.player.move(-1, 0)
        if keystate[pygame.K_RIGHT]:
            self.player.move(1, 0)
        if keystate[pygame.K_UP]:
            self.player.move(0, -1)
        if keystate[pygame.K_DOWN]:
            self.player.move(0, 1)
        if keystate[pygame.K_ESCAPE]:
            self.quit()

    def show_start_screen(self):
        pass


game = Game()
game.show_start_screen()

while True:
    game.reset()
    game.run()
