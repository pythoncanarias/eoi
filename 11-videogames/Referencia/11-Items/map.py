import random
from os import path

from settings import *
from sprites import *


class Map:
    def __init__(self):
        self.entry_point = (0, 0)
        self.map_data = []
        self.map_width = 0
        self.map_height = 0
        self.pixel_width = 0
        self.pixel_height = 0
        pass

    def load_from_file(self, filename):
        game_folder = path.dirname(__file__)
        self.map_file_data = []
        with open(path.join(game_folder, "data", filename), 'r') as f:
            for line in f:
                self.map_file_data.append(line)
        self.map_width = len(self.map_file_data[0]) - 1
        self.map_height = len(self.map_file_data)
        self.pixel_width = (self.map_width) * TILESIZE
        self.pixel_height = (self.map_height) * TILESIZE

        for row, rowLine in enumerate(self.map_file_data):
            row_data = []
            for col, colChar in enumerate(rowLine):
                row_data.append(colChar)
            self.map_data.append(row_data)

    def create_cave_cellular_automata(self, game, width, height):
        self.map_width = width
        self.map_height = height
        self.pixel_width = (self.map_width) * TILESIZE
        self.pixel_height = (self.map_height) * TILESIZE

        self.map_data = [
            ["1" if y == 0 or y == (height-1) or x == 0 or x == (width-1) else "0"
             for y in range(0, height)]
            for x in range(0, width)
        ]

        start_walls = (int)(width * height * 0.45)
        for i in range(0, start_walls):
            x = random.randint(1, width-1)
            y = random.randint(1, height-1)
            self.map_data[x][y] = "1"

        iterations = 10
        zoom = 4

        game.screen.fill(LIGHTGREY)
        pygame.display.flip()

        neighbour_deltas = [(x, y) for x in range(-1, 2)
                            for y in range(-1, 2) if x != 0 or y != 0]
        for j in range(0, iterations):
            tmp_map = self.map_data.copy()
            for x in range(1, width-1):
                for y in range(1, height-1):
                    sum = 0
                    for delta in neighbour_deltas:
                        dx, dy = delta
                        if self.map_data[x+dx][y+dy] == "1":
                            sum = sum + 1
                    if tmp_map[x][y] == "1":
                        tmp_map[x][y] = "1" if sum >= 3 else "0"
                    else:
                        tmp_map[x][y] = "1" if sum >= 5 else "0"

                    pygame.draw.rect(
                        game.screen,
                        DARKGREY if tmp_map[x][y] == "1" else LIGHTGREY,
                        (x * zoom, y * zoom, zoom, zoom)
                    )

            self.map_data = tmp_map.copy()

            pygame.display.flip()
            # pygame.time.wait(1000)

        player_pos = self.get_empty_position()
        self.map_data[int(player_pos.x)][int(player_pos.y)] = "P"

        for i in range(0, 5):
            pos = self.get_empty_position()
            self.map_data[int(pos.x)][int(pos.y)] = "B"

    def create_cave_diggers(self, game, width, height):
        self.map_width = width
        self.map_height = height
        self.pixel_width = (self.map_width) * TILESIZE
        self.pixel_height = (self.map_height) * TILESIZE

        self.map_data = [
            ["1" for y in range(0, height)]
            for x in range(0, width)
        ]

        iterations = int(width * height * 0.25)
        digger_count = 3
        diggers = [vec(width / 2, height / 2) for i in range(0, digger_count)]
        neighbour_deltas = [vec(-1, 0), vec(1, 0), vec(0, -1), vec(0, 1)]

        game.screen.fill(LIGHTGREY)
        pygame.display.flip()
        zoom = 4

        for _ in range(0, iterations):
            tmp_map = self.map_data.copy()
            for j in range(0, digger_count):
                direction = random.randint(0, len(neighbour_deltas)-1)
                diggers[j] = diggers[j] + neighbour_deltas[direction]
                diggers[j] = vec(
                    max(1, min(diggers[j].x, width - 1)),
                    max(1, min(diggers[j].y, height - 1))
                )
                tmp_map[int(diggers[j].x)][int(diggers[j].y)] = "0"

                pygame.draw.rect(
                    game.screen, DARKGREY, (diggers[j].x * zoom, diggers[j].y * zoom, zoom, zoom))

            self.map_data = tmp_map.copy()

            pygame.display.flip()
            # pygame.time.wait(1)

        clean_iterations = 1
        for _ in range(0, clean_iterations):
            tmp_map = self.map_data.copy()
            for x in range(1, width-1):
                for y in range(1, height-1):
                    sum = 0
                    for delta in neighbour_deltas:
                        dx, dy = delta
                        if self.map_data[int(x+dx)][int(y+dy)] == "1":
                            sum = sum + 1
                    if tmp_map[x][y] == "1":
                        tmp_map[x][y] = "1" if sum >= 2 else "0"
            self.map_data = tmp_map.copy()

        player_pos = self.get_empty_position()
        self.map_data[int(player_pos.x)][int(player_pos.y)] = "P"

        # for _ in range(0, 5):
        #    pos = self.get_empty_position()
        #    self.map_data[int(pos.x)][int(pos.y)] = "B"

    def get_empty_position(self):
        is_empty = False
        while is_empty == False:
            x = random.randint(1, self.map_width - 1)
            y = random.randint(1, self.map_height - 1)
            if self.map_data[x][y] == "0":
                return vec(x, y)

    def create_sprites_from_data(self, game):
        """We should add items here!!!"""
        for row in range(0, self.map_height):
            for col in range(0, self.map_width):
                tile = self.map_data[row][col]
                tile_south = self.map_data[row+1][col] if row + \
                    1 < self.map_height else tile
                x, y = col * TILESIZE, row * TILESIZE
                if tile == '1':
                    is_wall_top = tile == tile_south
                    Wall(game, x, y, is_wall_top)
                if tile == 'P':
                    self.entry_point = (x, y)
                if tile == 'B':
                    print(f"bee nest at {x},{y}")
                    BeeNest(game, x, y, (game.all_sprites,
                                         game.nests),
                            game.bee_nest_img,
                            BEE_NEST_MAX_HEALTH,
                            BEE_NEST_SPAWN_FREQUENCY,
                            BEE_NEST_MAX_POPULATION)
                if tile == 'b':
                    Bee(game, x, y, (game.all_sprites,
                                     game.mobs),
                        game.bee_img,
                        BEE_SPEED, BEE_HEALTH)
