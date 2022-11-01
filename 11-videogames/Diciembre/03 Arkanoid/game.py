import pygame
from settings import *
from sprites import *

from os import path


class Game:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 1024)
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption("ARKANOID")
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        root_folder = path.dirname(__file__)
        fx_folder = path.join(root_folder, "sound")
        img_folder = path.join(root_folder, "img")
        self.load_fx_and_music(fx_folder)
        self.load_images(img_folder)

    def load_fx_and_music(self, fx_folder):
        self.bounce_fx = pygame.mixer.Sound(path.join(fx_folder, "bounce.wav"))
        pygame.mixer.Sound.set_volume(self.bounce_fx, 0.3)
        self.break_fx = pygame.mixer.Sound(path.join(fx_folder, "break.wav"))
        pygame.mixer.Sound.set_volume(self.break_fx, 0.3)

    def load_images(self, img_folder):
        self.pad_image = pygame.image.load(
            path.join(img_folder, "paddleRed.png"))
        self.ball_image = pygame.image.load(
            path.join(img_folder, "ballBlue.png")
        )
        brick_colors = ["blue", "purple", "red", "yellow", "green", "grey"]
        self.brick_images = []
        for color in brick_colors:
            filename = f"element_{color}_rectangle.png"
            img = pygame.image.load(path.join(img_folder, filename))
            self.brick_images.append(img)

    def start(self):
        self.all_sprites = pygame.sprite.Group()
        self.bricks = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()
        self.create_stage()
        self.player = Player(self, WIDTH//2, HEIGHT-PAD_HEIGHT*2)
        self.ball = Ball(self, WIDTH//2, HEIGHT-PAD_HEIGHT*4)
        self.run()

    def create_stage(self):
        for x in range(0, 11):
            for y in range(0, 7):
                Brick(
                    self,
                    BRICK_WIDTH * 2.5 + x * BRICK_WIDTH + x * 5,
                    BRICK_HEIGHT * 2.5 + y * BRICK_HEIGHT + y * 5
                )

    def run(self):
        self.playing = True
        while (self.playing):
            self.dt = self.clock.tick(FPS)/1000
            self.events()
            self.update()
            self.draw()

        if len(self.bricks.sprites()) == 0:
            self.start()
        else:
            print("GAME OVER")

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.powerup_multiball()

    def update(self):
        self.update_collisions()
        self.all_sprites.update()

    def update_collisions(self):
        hits = pygame.sprite.spritecollide(self.player, self.balls, False)
        for ball in hits:
            ball.bounce(self.player)
            self.player.hit(ball)

        hits = pygame.sprite.groupcollide(
            self.balls, self.bricks, False, False)
        for ball, bricks in hits.items():
            the_brick = bricks[0]
            ball.bounce(the_brick)
            the_brick.hit()
            break

    def powerup_multiball(self):)
        for _ in range(10):
            reference=self.balls.sprites()[0]
            ball=Ball(self, reference.rect.centerx, reference.rect.centery)
            ball.velocity=Vector2(
                reference.velocity.x + random.uniform(-0.5, 0.5), reference.velocity.y)
            ball.isAsleep=False

    def ball_lost(self):
        self.ball=Ball(self, self.player.rect.centerx,
                         self.player.rect.top - 32)

    def draw(self):
        self.screen.fill(DARKGREY)
        self.all_sprites.draw(self.screen)

        pygame.display.flip()


game=Game()
game.start()
