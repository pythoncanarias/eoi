import pygame
from settings import *

from map import Map
from sprites import Player


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(GAME_TITLE)
        self.screen = pygame.display.set_mode(
            [WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        self.map = Map()
        self.map.load_from_file('map.txt')
        self.map.create_sprites_from_map_data(self)

        self.player = Player(self, self.map.player_entry_point)

    def start_game(self):
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def update(self):
        self.player.update()

    def draw(self):
        self.screen.fill(DARKGREEN)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()


game = Game()
game.start_game()
