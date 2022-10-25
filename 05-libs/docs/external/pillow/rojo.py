from PIL import Image

leon = Image.open("leon.jpg")
leon.thumbnail((350, 450))
r, g, b = leon.split()
r = r.point(lambda x: x*1.2)
g = g.point(lambda x: x*0.85)
b = b.point(lambda x: x*0.85)
rebuild = Image.merge("RGB", (r, g, b))
rebuild