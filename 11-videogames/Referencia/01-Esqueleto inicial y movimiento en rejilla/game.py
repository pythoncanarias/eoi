import pygame
import sys
from settings import *
from sprites import *


class Game:
    def __init__(self):
        """Create the game window, game clock and load required data."""
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        """No data to load at this point, so we just pass"""
        pass

    def reset(self):
        """Prepare sprite groups and main entities: player and in a near future, the map"""
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self, 10, 10)

    def run(self):
        """The Game Loop! Quite simple in a real-time game: read events, call logic updates, draw everything, rinse, repeat!"""
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)/1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        """Just quit the game and exit"""
        pygame.quit()
        sys.exit()

    def update(self):
        """Pygame sprites have an update method which should be responsible for updating the game logic."""
        self.all_sprites.update()

    def draw(self):
        """Drawing the game can be tricky, but right now we'll just clear with a plain color, draw a grid and all
        sprites in the all_sprites group. Don't forget to call flip so the buffer where sprites are drawn is 
        actually sent to the screen."""
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def draw_grid(self):
        """A quite handy function that will show the actual tile size of our tile-based game"""
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def events(self):
        """Event handling, but will be refactored in future lessons. After all, the player is the only entity that reads
        input events (except for Psycho Mantis)."""
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


game = Game()

while True:
    game.reset()
    game.run()
