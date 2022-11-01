import os

from PIL import Image

for fn in os.listdir():
    try:
        im = Image.open(fn)
        width, height = im.size
        print(f"{fn} {width}x{height} {im.mode}")
    except IOError:
        pass
