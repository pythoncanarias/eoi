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
# Tilesize must coincide with map's size!
TILESIZE = 21

# player
# Now we are using natural ticks, so instead of 250 we'll move at 0.25
PLAYER_SPEED = 0.25
