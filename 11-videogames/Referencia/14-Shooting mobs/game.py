#
# ART:  https://kenney.nl/assets/platformer-art-pixel-redux
#

import pygame
import sys
from os import path

from settings import *
from mobs import *
from spritesheet import Spritesheet
from map import Map
from camera import Camera


class Game:
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
        """Let's create more sensible data structures for each group"""
        root_folder = path.dirname(__file__)
        img_folder = path.join(root_folder, "data", "img")
        music_folder = path.join(root_folder, "data", "music")
        fx_folder = path.join(root_folder, "data", "fx")

        sprites = Spritesheet(
            path.join(img_folder, "spritesheet_x2.png"))

        # IMAGES & SOUND

        self.images = {}
        self.fx = {}

        for item in ITEMS:
            sprite_at = ITEMS[item]['SPRITE']
            self.images[item] = sprites.image_at(
                sprite_at[0], sprite_at[1], TILESIZE, 2, KEY_COLOR)
            fx = pygame.mixer.Sound(
                path.join(fx_folder, ITEMS[item]['FX_PICKUP']))
            fx.set_volume(0.1)
            self.fx[item] = fx

        for mob in MOBS:
            sprite_at = MOBS[mob]['SPRITE']
            self.images[mob] = sprites.image_at(
                sprite_at[0], sprite_at[1], TILESIZE, 2, KEY_COLOR)
            fx = pygame.mixer.Sound(
                path.join(fx_folder, MOBS[mob]['FX_DEATH']))
            fx.set_volume(0.1)
            self.fx[mob] = fx

        for nest in NESTS:
            sprite_at = NESTS[nest]['SPRITE']
            self.images[nest] = sprites.image_at(
                sprite_at[0], sprite_at[1], TILESIZE, 2, KEY_COLOR)
            fx = pygame.mixer.Sound(
                path.join(fx_folder, NESTS[nest]['FX_DEATH']))
            fx.set_volume(0.1)
            self.fx[nest] = fx

        for weapon in WEAPONS:
            fx = pygame.mixer.Sound(
                path.join(fx_folder, WEAPONS[weapon]['FX']))
            fx.set_volume(0.1)
            self.fx[weapon] = fx

        self.tiles = {}
        for wall in WALLS:
            for orientation in ['TOP', 'FRONT']:
                sprite_at = WALLS[wall][orientation]
                self.tiles[f"{wall}_{orientation}"] = sprites.image_at(
                    sprite_at[0], sprite_at[1], TILESIZE, 2, KEY_COLOR)

        # MUSIC
        pygame.mixer.music.load(path.join(music_folder, BG_MUSIC))

    def reset(self):
        """Creating enemy bullet group, adding gun to constructors"""
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
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
            self.images['PLAYER'],
            MOBS['PLAYER']['SPEED'],
            MOBS['PLAYER']['HEALTH'],
            'GUN')

        HealthPack(self,
                   self.player.pos.x + TILESIZE,
                   self.player.pos.y + TILESIZE)

        SpeedUp(self,
                self.player.pos.x - TILESIZE,
                self.player.pos.y - TILESIZE)

        self.camera = Camera(self.current_map.pixel_width,
                             self.current_map.pixel_height)

    def run(self):
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
        """Adding player-enemybullets collisions and updating player_bullets"""
        self.all_sprites.update()
        self.camera.update(self.player)

        # bullets hitting nests
        hits = pygame.sprite.groupcollide(
            self.nests, self.player_bullets, False, True)
        for nest, bullets in hits.items():
            nest.hit(bullets[0].damage)

        # bullets hitting mobs
        hits = pygame.sprite.groupcollide(
            self.mobs, self.player_bullets, False, True)
        for mob, bullets in hits.items():
            mob.hit(bullets[0].damage)

        # bullets hitting player
        hits = pygame.sprite.spritecollide(
            self.player, self.enemy_bullets, True)
        for bullet in hits:
            self.player.hit(bullet.damage)

        # mobs hitting player
        hits = pygame.sprite.spritecollide(
            self.player, self.mobs, False)
        for mob in hits:
            mob.attack(self.player)

        # player hitting items
        hits = pygame.sprite.spritecollide(
            self.player, self.items, False)
        for item in hits:
            item.picked_by(self.player)

    def draw(self):
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(DARKGREY)
        for sprite in self.all_sprites:
            if isinstance(sprite, Mob) and sprite != self.player:
                sprite.draw_health()
                in_camera = self.camera.apply_to_sprite(sprite)

            self.screen.blit(sprite.image, self.camera.apply_to_sprite(sprite))

            # pygame.draw.rect(self.screen, YELLOW,
            #                self.camera.apply_to_sprite(sprite))

        self.draw_player_health(self.screen, 10, 10,
                                self.player.health / MOBS['PLAYER']['HEALTH'])
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
