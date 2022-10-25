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

        self.large_font = pygame.font.SysFont('arial', 100)
        self.small_font = pygame.font.SysFont('arial', 32)

    def start(self):
        self.all_sprites = pygame.sprite.Group()
        self.fruits = pygame.sprite.Group()
        self.player = Player(self, 10, 10)
        self.fruit = Fruit(self)
        self.score = 0
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
            self.playing = False
            self.game_over()

    def draw(self):
        self.screen.fill(DARKGREY)
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

        self.all_sprites.draw(self.screen)
        self.player.draw_tail(self.screen)

        score_text = self.small_font.render(
            f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        # Nothing else to draw, let's show it!
        pygame.display.flip()

    #
    #   MAIN MENU AND GAME OVER SCREENS
    #

    def main_menu(self):
        title_text = self.large_font.render("SNAKE", True, WHITE)
        instructions_text = self.small_font.render(
            "Press any key to begin", True, WHITE)

        self.screen.fill(BLACK)
        self.screen.blit(
            title_text, (WIDTH//2 - title_text.get_rect().centerx, HEIGHT//2 - title_text.get_rect().centery))
        self.screen.blit(
            instructions_text, (WIDTH//2 -
                                instructions_text.get_rect().centerx, HEIGHT//2 + 150))
        pygame.display.flip()
        pygame.time.delay(1000)
        in_main_menu = True
        while in_main_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    in_main_menu = False
        self.start()

    def game_over(self):
        title_text = self.large_font.render("GAME OVER", True, WHITE)
        score_text = self.small_font.render(
            f"Score: {self.score}  (Press any key to continue)", True, WHITE)

        self.screen.fill(BLACK)
        self.screen.blit(
            title_text, (WIDTH//2 - title_text.get_rect().centerx, HEIGHT//2 - title_text.get_rect().centery))
        self.screen.blit(
            score_text, (WIDTH//2 -
                         score_text.get_rect().centerx, HEIGHT//2 + 150))
        pygame.display.flip()
        pygame.time.delay(1000)
        in_gameover_menu = True
        while in_gameover_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    in_gameover_menu = False
        self.main_menu()


game = Game()
game.main_menu()
