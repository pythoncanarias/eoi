import pygame
from settings import *
from map import Map
from sprites import Player


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption("PEWPEWPEW")
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        pass

    def start(self):
        self.mobs = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.current_map = Map()
        self.current_map.load_map_from_file("map.txt")
        self.current_map.create_sprites_from_data(self)
        self.player = Player(
            self,
            self.current_map.entry_point.x,
            self.current_map.entry_point.y
        )
        self.run()

    def run(self):
        self.playing = True
        while (self.playing):
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
        self.mobs.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.walls.draw(self.screen)
        self.mobs.draw(self.screen)
        pygame.display.flip()


game = Game()
game.start()
