# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 640   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 480  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY

# map
# ADDED Duplicated tile size to make things bigger
TILESIZE = 42
KEY = (94, 129, 162)

# player
PLAYER_SPEED = 0.25
PLAYER_SPRITE_AT = (28, 0)
# ADDED Player's health
PLAYER_HEALTH = 100


# walls, purplish
TOP_WALL_SPRITE_AT = (4, 24)
FRONT_WALL_SPRITE_AT = (4, 25)

# Bee
BEE_SPEED = 0.1
BEE_SPRITE_AT = (24, 11)
# ADDED HEALTH AND KNOCKBACK WHEN ATTACK
BEE_HEALTH = 10
BEE_KNOCKBACK = 0.1

# Basic gun
BASIC_GUN_SPEED = 0.5
BASIC_GUN_FIRING_RATE = 100
BASIC_GUN_COLOR = YELLOW
BASIC_GUN_TTL = 2000
BASIC_GUN_SPREAD = 0.1
# ADDED GUN DAMAGE
BASIC_GUN_DAMAGE = 1
