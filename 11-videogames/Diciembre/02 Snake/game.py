from settings import *
import pygame
import sys
import random
import math

from sprites import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_assets()

    def load_assets(self):
        self.large_font = pygame.font.SysFont('arial', 100)
        self.small_font = pygame.font.SysFont('arial', 32)

    def start_game(self):
        self.reset()
        self.run()

    def reset(self):
        self.snake = Snake(self, GRIDWIDTH//2, GRIDHEIGHT//2)
        self.fruit = Fruit()
        self.score = 0

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.event()
            self.update()
            self.draw()
        self.game_over()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.snake.update()
        self.playing = self.playing and self.snake.isAlive

        hit = pygame.sprite.collide_rect(self.snake, self.fruit)
        if hit:
            self.snake.grow()
            self.fruit.teleport_to_random_position()
            self.score += 1

    def draw(self):
        self.draw_grid()
        self.draw_mobs()
        self.draw_HUD()
        pygame.display.flip()

    def draw_mobs(self):
        self.snake.draw(self.screen)
        self.fruit.draw(self.screen)

    def draw_HUD(self):
        score_text = self.small_font.render(
            f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

    def draw_grid(self):
        self.screen.fill(BGCOLOR)
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, DARKGREY, (x, 0), (x, HEIGHT), 1)
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, DARKGREY, (0, y), (WIDTH, y), 1)

    #
    #   MAIN MENU AND GAME OVER SCREENS
    #

    def main_menu(self):
        title_text = self.large_font.render("SNAKE", True, WHITE)
        instructions_text = self.small_font.render(
            "Pulsa una tecla para empezar", True, LIGHTGREY)

        self.screen.fill(BGCOLOR)
        self.screen.blit(
            title_text,
            (WIDTH//2 - title_text.get_rect().centerx,
             HEIGHT//2 - title_text.get_rect().centery))
        self.screen.blit(
            instructions_text,
            (WIDTH//2 - instructions_text.get_rect().centerx,
             HEIGHT//2 - instructions_text.get_rect().centery + 64))
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
        self.start_game()

    def game_over(self):
        title_text = self.large_font.render("GAME OVER", True, WHITE)
        instructions_text = self.small_font.render(
            f"Score: {self.score} (press any key to continue)", True, LIGHTGREY)

        self.screen.fill(BGCOLOR)
        self.screen.blit(
            title_text,
            (WIDTH//2 - title_text.get_rect().centerx,
             HEIGHT//2 - title_text.get_rect().centery))
        self.screen.blit(
            instructions_text,
            (WIDTH//2 - instructions_text.get_rect().centerx,
             HEIGHT//2 - instructions_text.get_rect().centery + 64))
        pygame.display.flip()

        pygame.time.delay(1000)

        in_game_over = True
        while in_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    in_game_over = False
        self.main_menu()


game = Game()
game.main_menu()
