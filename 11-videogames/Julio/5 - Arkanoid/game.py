import pygame
from settings import *
from sprites import *

from os import path


class Game:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 1024)
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(GAME_TITLE)
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        root_folder = path.dirname(__file__)
        img_folder = path.join(root_folder, "img")
        fx_folder = path.join(root_folder, "sound")

        # Load images
        brick_colors = ['blue', 'green', 'grey', 'purple', 'red', 'yellow']
        self.brick_images = []
        for color in brick_colors:
            img = pygame.image.load(
                path.join(img_folder, f"element_{color}_rectangle.png")).convert_alpha()
            self.brick_images.append(img)
        self.ball_image = pygame.image.load(
            path.join(img_folder, "ballBlue.png")).convert_alpha()
        self.pad_image = pygame.image.load(
            path.join(img_folder, "paddleBlu.png")).convert_alpha()

        # Load FX and MUSIC
        self.bounce_fx = pygame.mixer.Sound(path.join(fx_folder, 'bounce.wav'))
        self.break_fx = pygame.mixer.Sound(path.join(fx_folder, 'break.wav'))
        pygame.mixer.music.load(path.join(fx_folder, 'Adventure.mp3'))

    def start_game(self):
        self.all_sprites = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()
        self.bricks = pygame.sprite.Group()

        self.player = Pad(self, WIDTH // 2, HEIGHT - 64)
        self.ball = Ball(self, WIDTH // 2, HEIGHT - 128)
        self.build_brick_wall()
        self.run()

    def build_brick_wall(self):
        brick_width = self.brick_images[0].get_rect().width
        brick_height = self.brick_images[0].get_rect().height
        for x in range(8):
            for y in range(7):
                brick_x = 90 + brick_width * x + 2*x
                brick_y = 50 + brick_height * y + 2*y
                Brick(self, brick_x, brick_y)

    def run(self):
        self.playing = True
        # pygame.mixer.music.play(-1)
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
                    self.multi_ball_powerup()

    def update(self):
        self.all_sprites.update()

    def hitbox_collide(self, sprite, other):
        return sprite.hitbox.colliderect(other.hitbox)

    def multi_ball_powerup(self):
        if len(self.balls.sprites()) == 0:
            return

        reference = self.balls.sprites()[0]
        if reference.asleep:
            return

        for _ in range(MULTIBALL_POWERUP):
            ball = Ball(self, reference.position.x, reference.position.y)
            ball.velocity = Vector2(
                reference.velocity.x *
                random.uniform(-0.5, 0.5),
                reference.velocity.y * random.uniform(0.75, 1.25))
            ball.asleep = False

    def ball_lost(self):
        if len(self.balls.sprites()) == 0:
            self.player.velocity = Vector2(0, 0)
            self.ball = Ball(self, self.player.rect.centerx,
                             self.player.rect.top - 32)
            self.in_game_balls = 1

    def draw(self):
        self.screen.fill(DARKBLUE)
        self.all_sprites.draw(self.screen)

        # DEBUG
        # for sprite in self.all_sprites:
        #    pygame.draw.rect(self.screen, (0, 230, 0), sprite.rect, 2)
        #    pygame.draw.rect(self.screen, (250, 30, 0), sprite.hitbox, 2)

        pygame.display.flip()


game = Game()
game.start_game()
