WIDTH = 640
HEIGHT = 480
FPS = 30

TILESIZE = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (32, 32, 32)
LIGHTGREY = (198, 198, 198)
RED = (255, 0, 0)
DARKRED = (64, 0, 0)
GREEN = (25, 200, 25)
DARKGREEN = (25, 125, 25)
BLUE = (25, 25, 200)
BROWN = (80, 40, 12)
ORANGE = (255, 128, 0)
YELLOW = (250, 250, 0)
PALE_RED = (200, 64, 64)
CAUCASIAN_SKIN = (238, 195, 154)

GRAVITY = 1000
TERMINAL_VELOCITY = 500

PLAYER_SPEED = 250
PLAYER_JUMP_FORCE = 250
PLAYER_HEALTH = 100

DOUBLEJUMP_AVAILABLE = 2
DOUBLEJUMP_READY = 1
DOUBLEJUMP_UNAVAILABLE = 0

WASP_SPEED = 50
WASP_HEALTH = 25
WASP_DAMAGE = 1

WASP_NEST_HEALTH = 100
WASP_NEST_SPAWN_FREQ = 1000
WASP_NEST_MAX_POPULATION = 5

WEAPONS = {
    'GUN': {
        'SPEED': 500,
        'FIRING_RATE': 300,
        'COLOR': ORANGE,
        'TTL': 1000,
        'SPREAD': 0.1,
        'DAMAGE': 2,
        'AMMO_PER_SHOT': 1
    },
    'SHOTGUN': {
        'SPEED': 500,
        'FIRING_RATE': 600,
        'COLOR': ORANGE,
        'TTL': 250,
        'SPREAD': 0.3,
        'DAMAGE': 2,
        'AMMO_PER_SHOT': 10
    },
    'GATLING': {
        'SPEED': 500,
        'FIRING_RATE': 100,
        'COLOR': ORANGE,
        'TTL': 500,
        'SPREAD': 0.1,
        'DAMAGE': 1,
        'AMMO_PER_SHOT': 2
    }
}

ITEMS = {
    'HEALTH': {
        'COLOR': RED,
        'HEAL': 25
    },
    'WEAPONCRATE': {
        'COLOR': LIGHTGREY,
        'WEAPONS': ['SHOTGUN', 'GATLING']
    }
}
