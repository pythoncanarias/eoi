GAME_TITLE = "PEWPEWPEW"
WIDTH = 640
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 100, 100)
GREEN = (100, 200, 100)
DARKGREEN = (10, 20, 10)
BLUE = (100, 100, 200)
DARKBLUE = (25, 25, 50)
YELLOW = (200, 200, 100)
ORANGE = (200, 150, 100)
DARKORANGE = (100, 75, 50)
PURPLE = (182, 56, 157)

TILESIZE = 16

DRAG = 10
AVOID_RADIUS = 50

PLAYER_MAX_SPEED = 100
PLAYER_ACCELERATION = 2000
PLAYER_HEALTH = 100

BEE_MAX_SPEED = 50
BEE_ACCELERATION = 1000
BEE_HEALTH = 10
BEE_HIT_DAMAGE = 10

BEE_NEST_SPAWN_FREQUENCY = 5000
BEE_NEST_MAX_POPULATION = 5
BEE_NEST_HEALTH = 100
BEE_VISION_RADIUS = 150

MOBS = {
    'TOWER': {
        'HEALTH': 100,
        'COLOR': PURPLE,
        'WEAPON_NAME': 'GUN'
    }
}

ITEM_HOVER_SPEED = 0.01
ITEMS = {
    'HEALTHPACK': {
        'HEAL': 20,
        'FX': 'heal.wav',
        'COLOR': RED
    },
    'SPEEDUP': {
        'SPEED': 50,
        'TTL': 3000,
        'COLOR': BLUE
    }
}

WEAPONS = {
    'GUN': {
        'FIRING_RATE': 250,
        'SPREAD': 0.1,
        'TTL': 2000,
        'SPEED': 300,
        'DAMAGE': 5,
        'COLOR': RED,
        'SIZE': 10,
        'AMMO_PER_SHOT': 1,
        'FX': "pewpew.wav"
    },
    'MACHINEGUN': {
        'FIRING_RATE': 100,
        'SPREAD': 0.1,
        'TTL': 1500,
        'SPEED': 300,
        'DAMAGE': 2,
        'COLOR': RED,
        'SIZE': 8,
        'AMMO_PER_SHOT': 1,
        'FX': "pewpew.wav"
    },
    'SHOTGUN': {
        'FIRING_RATE': 1000,
        'SPREAD': 0.5,
        'TTL': 500,
        'SPEED': 300,
        'DAMAGE': 10,
        'COLOR': RED,
        'SIZE': 8,
        'AMMO_PER_SHOT': 10,
        'FX': "kaboom.wav"
    }
}
