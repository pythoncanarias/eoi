from PIL import Image, ImageDraw

leon = Image.open("leon.jpg")

width, height = leon.size
x, y = width //2, height // 2
y += 80
rect = (x-55, y-55, x+55, y+55)
draw = ImageDraw.Draw(leon)
draw.ellipse(rect, fill=(255, 0, 0), width=3)
leon.show()
