from PIL import Image, ImageDraw

leon = Image.open("leon.jpg")
leon.thumbnail((400, 400))
width, height = leon.size
draw = ImageDraw.Draw(leon)
for x in range(0, width, 32):
    draw.line((x, 0, x, height), fill="white", width=5)
for y in range(0, height, 32):
    draw.line((0, y, width, y), fill="white", width=5)
leon.show()
