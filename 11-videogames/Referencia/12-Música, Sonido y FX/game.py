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
    """Adding pygame mixer, which needs to be tweaked
    in order to avoid lag"""

    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 1024)
        pygame.init()
        pygame.mixer.set_num_channels(16)
        self.screen = pygame.display.set_mode(
            [WIDTH, HEIGHT])  # pygame.FULLSCREEN | pygame.DOUBLEBUF
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        """Adding music & fx"""
        root_folder = path.dirname(__file__)
        img_folder = path.join(root_folder, "data", "img")
        music_folder = path.join(root_folder, "data", "music")
        fx_folder = path.join(root_folder, "data", "fx")

        sprites = Spritesheet(
            path.join(img_folder, "spritesheet_x2.png"))

        # IMAGES

        self.item_images = {}
        for item_name in ITEMS:
            sprite_at = ITEMS[item_name]['SPRITE_AT']
            self.item_images[item_name] = sprites.image_at(
                sprite_at[0], sprite_at[1], TILESIZE, 2, KEY_COLOR)

        self.player_img = sprites.image_at(
            PLAYER_SPRITE_AT[0], PLAYER_SPRITE_AT[1], TILESIZE, 2, KEY_COLOR)

        self.bee_img = sprites.image_at(
            BEE_SPRITE_AT[0], BEE_SPRITE_AT[1], TILESIZE, 2, KEY_COLOR)

        self.bee_nest_img = sprites.image_at(
            BEE_NEST_SPRITE_AT[0], BEE_NEST_SPRITE_AT[1], TILESIZE, 2, KEY_COLOR)

        self.top_wall_img = sprites.image_at(
            TOP_WALL_SPRITE_AT[0], TOP_WALL_SPRITE_AT[1], TILESIZE, 2, KEY_COLOR)

        self.front_wall_img = sprites.image_at(
            FRONT_WALL_SPRITE_AT[0], FRONT_WALL_SPRITE_AT[1], TILESIZE, 2, KEY_COLOR)

        # SOUND
        # Using arrays to add some variance
        pygame.mixer.music.load(path.join(music_folder, BG_MUSIC))
        self.basic_gun_fx = []
        for fx in BASIC_GUN_FX:
            pewpew = pygame.mixer.Sound(path.join(fx_folder, fx))
            pewpew.set_volume(0.1)
            self.basic_gun_fx.append(pewpew)
        self.critter_death_fx = []
        for fx in CRITTER_DEAD_FX:
            self.critter_death_fx.append(
                pygame.mixer.Sound(path.join(fx_folder, fx)))
        self.item_fx = {}
        for fx in ITEMS:
            self.item_fx[fx] = pygame.mixer.Sound(
                path.join(fx_folder, ITEMS[fx]['FX']))

    def reset(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.nests = pygame.sprite.Group()
        self.items = pygame.sprite.Group()

        self.current_map = Map()
        self.current_map.load_from_file("bigMap.txt")
        # self.current_map.create_cave_cellular_automata(self, 50, 50)
        # self.current_map.create_cave_diggers(self, 50, 50)

        self.current_map.create_sprites_from_data(self)

        self.player = Player(
            self,
            self.current_map.entry_point[0], self.current_map.entry_point[1],
            self.all_sprites,
            self.player_img,
            PLAYER_SPEED,
            PLAYER_HEALTH)

        HealthPack(self,
                   self.player.pos.x + TILESIZE,
                   self.player.pos.y + TILESIZE)

        SpeedUp(self,
                self.player.pos.x - TILESIZE,
                self.player.pos.y - TILESIZE)

        self.camera = Camera(self.current_map.pixel_width,
                             self.current_map.pixel_height)

    def run(self):
        """Start playing music!"""
        self.playing = True
        # pygame.mixer.music.play(loops=-1)
        while self.playing:
            self.dt = self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

        # bullets hitting nests
        hits = pygame.sprite.groupcollide(
            self.nests, self.bullets, False, True)
        for nest, bullets in hits.items():
            nest.hit(bullets[0].damage)

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

        # player hitting items
        hits = pygame.sprite.spritecollide(
            self.player, self.items, False, False)
        for item in hits:
            item.picked_by(self.player)

    def draw(self):
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(DARKGREY)
        for sprite in self.all_sprites:
            if isinstance(sprite, Mob) and sprite != self.player:
                sprite.draw_health()

            self.screen.blit(sprite.image, self.camera.apply_to_sprite(sprite))

            # pygame.draw.rect(self.screen, YELLOW,
            #                self.camera.apply_to_sprite(sprite))

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
