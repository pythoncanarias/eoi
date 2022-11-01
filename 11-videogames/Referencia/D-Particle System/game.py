import pygame
import sys
from settings import *
from pygame import Vector2
import random


class Particle(pygame.sprite.Sprite):
    """Particles have a position, velocity, drag, ttl, color and size
    They require game to have a particles group"""

    def __init__(self, game, position, velocity, drag, gravity, ttl, color, size):
        self.game = game
        pygame.sprite.Sprite.__init__(self, game.particles)
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.original_image = self.image
        self.rect = self.image.get_rect()

        self.rect.center = position
        self.position = position
        self.velocity = velocity
        self.gravity = gravity
        self.drag = drag
        self.ttl = ttl
        self.color = color
        self.size = size
        self.birth_time = pygame.time.get_ticks()

    def update(self):
        self.position += (self.velocity + self.gravity *
                          Vector2(0, 1)) * self.game.dt
        self.rect.center = self.position

        self.velocity *= self.drag

        t = (pygame.time.get_ticks() - self.birth_time)
        size = max(0, round((1 - (t / self.ttl)) * self.rect.width))
        self.image = pygame.transform.scale(
            self.original_image, (size, size))
        if t >= self.ttl:
            self.kill()


class ParticleSystem (pygame.sprite.Sprite):
    """If ParticlySystems are sprites we can call update while they are alive.
    Game needs to have a particle_systems group"""

    def __init__(self, game, position, min_max_velocity, min_max_drag, gravity, min_max_ttl, color, min_max_size, burst_particles, loop_time):
        pygame.sprite.Sprite.__init__(self, game.particle_systems)
        self.game = game
        self.position = position
        self.min_max_velocity = min_max_velocity
        self.min_max_drag = min_max_drag
        self.gravity = gravity
        self.min_max_ttl = min_max_ttl
        self.color = color
        self.min_max_size = min_max_size
        self.last_spawn_time = pygame.time.get_ticks()
        self.burst_particles = burst_particles
        self.loop_time = loop_time
        self.isAlive = True
        self.spawn_particles()

    def update(self):
        if pygame.time.get_ticks() - self.last_spawn_time > self.loop_time:
            self.spawn_particles()

    def spawn_particles(self):
        for _ in range(0, self.burst_particles):
            position = Vector2(self.position.x, self.position.y)
            velocity = Vector2(random.uniform(self.min_max_velocity[0].x, self.min_max_velocity[1].x),
                               random.uniform(self.min_max_velocity[0].y, self.min_max_velocity[1].y))
            drag = random.uniform(self.min_max_drag[0], self.min_max_drag[1])
            gravity = self.gravity
            ttl = random.uniform(self.min_max_ttl[0], self.min_max_ttl[1])
            size = random.uniform(self.min_max_size[0], self.min_max_size[1])
            Particle(self.game, position, velocity,
                     drag, gravity, ttl, self.color, size)
        self.last_spawn_time = pygame.time.get_ticks()

        if self.loop_time == -1:
            self.kill()


class Game:
    def __init__(self):
        """Create the game window, game clock and load required data."""
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def reset(self):
        """Prepare sprite groups and main entities"""
        self.particles = pygame.sprite.Group()
        self.particle_systems = pygame.sprite.Group()
        pass

    def run(self):
        """The Game Loop! Quite simple in a real-time game: read events, call logic updates, draw everything, rinse, repeat!"""
        self.playing = True
        while self.playing:
            self.dt = 1/self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        """Pygame sprites have an update method which should be responsible for updating the game logic."""
        self.particle_systems.update()
        self.particles.update()

    def events(self):
        """Event handling"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ParticleSystem(self,
                                   position=Vector2(WIDTH/2, HEIGHT/2),
                                   min_max_velocity=(
                                       Vector2(-100, -200), Vector2(100, 0)),
                                   min_max_drag=(0.95, 0.99),
                                   gravity=98,
                                   min_max_ttl=(1500, 2000),
                                   color=RED,
                                   min_max_size=(10, 25),
                                   burst_particles=50,
                                   loop_time=-1)

    def draw(self):
        """Drawing the game can be tricky, but right now we'll just clear with a plain color, draw bricks, pad,
        ball and score and flip the buffer. """
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.particles.draw(self.screen)
        pygame.display.flip()

    def quit(self):
        """Just quit the game and exit"""
        pygame.quit()
        sys.exit()

    def draw_grid(self):
        """A quite handy function that will show the actual tile size of our tile-based game"""
        for x in range(0, WIDTH, BRICK_WIDTH):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, BRICK_HEIGHT):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))


game = Game()

while True:
    game.reset()
    game.run()
