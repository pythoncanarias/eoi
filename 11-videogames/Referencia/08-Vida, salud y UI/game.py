#
# ART:  https://kenney.nl/assets/platformer-art-pixel-redux
#

import pygame
import sys
from os import path

from settings import *
from sprites import *
from spritesheet import Spritesheet
from map import Map
from camera import Camera


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            [WIDTH, HEIGHT])  # pygame.FULLSCREEN | pygame.DOUBLEBUF
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        """Using a bigget spritesheet, twice as big"""
        root_folder = path.dirname(__file__)

        sprites = Spritesheet(
            path.join(root_folder, "data", "img", "spritesheet_x2.png"))

        self.player_img = sprites.image_at(
            PLAYER_SPRITE_AT[0], PLAYER_SPRITE_AT[1], TILESIZE, 2, KEY)

        self.bee_img = sprites.image_at(
            BEE_SPRITE_AT[0], BEE_SPRITE_AT[1], TILESIZE, 2, KEY)

        self.top_wall_img = sprites.image_at(
            TOP_WALL_SPRITE_AT[0], TOP_WALL_SPRITE_AT[1], TILESIZE, 2, KEY)
        self.front_wall_img = sprites.image_at(
            FRONT_WALL_SPRITE_AT[0], FRONT_WALL_SPRITE_AT[1], TILESIZE, 2, KEY)

    def reset(self):
        """MOBs have health now. Also the player"""
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.current_map = Map()
        self.current_map.load_from_file("bigMap.txt")
        self.current_map.create_sprites_from_data(self)

        self.player = Player(
            self,
            self.current_map.entry_point[0], self.current_map.entry_point[1],
            self.all_sprites,
            self.player_img,
            PLAYER_SPEED,
            PLAYER_HEALTH)

        self.camera = Camera(self.current_map.pixel_width,
                             self.current_map.pixel_height)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        """Resolve sprite collisions. Bullets, melee, pushing..."""
        self.all_sprites.update()
        self.camera.update(self.player)

        # bullets hitting mobs
        hits = pygame.sprite.groupcollide(self.mobs, self.bullets, False, True)
        for mob, bullets in hits.items():
            mob.hit(bullets[0].damage)

        # mobs hitting player
        hits = pygame.sprite.spritecollide(
            self.player, self.mobs, False, False)
        for mob in hits:
            mob.attack(self.player)

        # mobs hitting mobs
        hits = pygame.sprite.groupcollide(
            self.mobs, self.mobs, False, False)
        for mobA, mobB in hits.items():
            mobA.push(mobB[0])

    def draw(self):
        """Draw health bars on mobs and Game UI on top-left"""
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(DARKGREY)
        for sprite in self.all_sprites:
            if isinstance(sprite, Mob) and sprite != self.player:
                sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply_to_sprite(sprite))
        self.draw_player_health(self.screen, 10, 10,
                                self.player.health / PLAYER_HEALTH)
        pygame.display.flip()

    def draw_player_health(self, surface, x, y, health):
        if health < 0:
            health = 0
        BAR_LENTH = 100
        BAR_HEIGHT = 20
        fill = health * BAR_LENTH
        outline = pygame.Rect(x, y, BAR_LENTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        if health > 0.6:
            col = GREEN
        elif health > 0.3:
            col = YELLOW
        else:
            col = RED
        pygame.draw.rect(surface, col, fill_rect)
        pygame.draw.rect(surface, WHITE, outline, 2)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

    def show_start_screen(self):
        pass


game = Game()
game.show_start_screen()

while True:
    game.reset()
    game.run()
