import pygame
import math
from settings import *
from sprites import Player, Fruit


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)

        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("comicsansms", 24)

        self.all_sprites = pygame.sprite.Group()
        self.fruits = pygame.sprite.Group()

        self.reset()

    def reset(self):
        self.all_sprites.empty()
        self.fruits.empty()
        self.player = Player(self, 10, 10)
        self.fruit = Fruit(self)
        self.score = 0

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
                self.playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.grow()

    def update(self):
        self.all_sprites.update()
        hits = pygame.sprite.spritecollide(
            self.player, self.fruits, False)
        for fruit in hits:
            self.player.grow()
            fruit.teleport()
            self.score += 1

        if self.player.alive == False:
            self.reset()

    def draw(self):
        self.screen.fill(DARKGREY)
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

        self.all_sprites.draw(self.screen)
        self.player.draw_tail(self.screen)

        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        # Nothing else to draw, let's show it!
        pygame.display.flip()


game = Game()
game.run()
