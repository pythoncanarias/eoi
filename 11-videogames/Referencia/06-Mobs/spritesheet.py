import pygame


class Spritesheet(object):
    """Just a handy class to simplify loading a sprite from a sprite sheet"""

    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as message:
            print('Unable to load spritesheet image:', filename)
            raise SystemExit(message)

    def image_at(self, x, y, tilesize, offset, colorkey=None):
        """Creates an image from a spritesheet"""
        rect = pygame.Rect(
            offset * (1 + x) + x * tilesize + x * offset,
            offset * (1 + y) + y * tilesize + y * offset, tilesize, tilesize)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(self, rects, colorkey=None):
        """"Loads multiple images, supply a list of rects. Can be handy for animations!"""
        return [self.image_at(rect, colorkey) for rect in rects]
