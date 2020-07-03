# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 200, 0)

# game settings
WIDTH = 640   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 480  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY

MAX_SPEED = 5
# ADDED Some AI behaviour too to avoid pals
AVOID_RADIUS = 25

# map
TILESIZE = 42
KEY_COLOR = (94, 129, 162)

# walls, purplish
WALLS = {
    'REGULAR_WALL': {
        'TOP': (4, 23),
        'FRONT': (4, 25)
    }
}

# Bee
MOBS = {
    'PLAYER': {
        'SPEED': 4,
        'ACCELERATION': 1,
        'HEALTH': 100,
        'SPRITE': (28, 0),
        'FX_DEATH': "splat.wav"
    },
    'BEE': {
        'SPEED': 2,
        'ACCELERATION': 0.2,
        'HEALTH': 10,
        'VISION_RADIUS': 150,
        'KNOCKBACK': 1,
        'SPRITE': (24, 11),
        'FX_DEATH': "splat.wav"
    }
}

# Bee Nest
NESTS = {
    'BEENEST': {
        'SPAWN_FREQUENCY': 3000,
        'HEALTH': 25,
        'MAX_POPULATION': 5,
        'SPRITE': (24, 11),
        'FX_DEATH': "splat.wav"
    }
}

WEAPONS = {
    'GUN': {
        'SPEED': 0.5,
        'FIRING_RATE': 100,
        'COLOR': YELLOW,
        'TTL': 2000,
        'SPREAD': 0.1,
        'DAMAGE': 2,
        'AMMO_PER_SHOT': 1,
        'FX': "pewpew.wav"
    },
    'SHOTGUN': {
        'SPEED': 0.7,
        'FIRING_RATE': 1000,
        'COLOR': ORANGE,
        'TTL': 250,
        'SPREAD': 0.25,
        'DAMAGE': 10,
        'AMMO_PER_SHOT': 10,
        'FX': "pewpew5.wav"
    }
}

# Items
ITEM_HOVER_RANGE = 5
ITEM_HOVER_SPEED = 0.005
ITEMS = {
    'HEALTH': {
        'SPRITE': (13, 12),
        'HEAL': 20,
        'FX_PICKUP': 'heal.wav'
    },
    'SPEEDUP': {
        'SPRITE': (6, 29),
        'SPEED': 4,
        'DURATION': 3000,
        'FX_PICKUP': 'speedup.wav'
    }
}

# MUSIC
BG_MUSIC = "DST-RailJet-LongSeamlessLoop.ogg"
