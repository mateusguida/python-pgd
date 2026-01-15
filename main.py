from PIL import Image, ImageDraw
import random
from star import Star

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 720
HEIGHT = 1280

img = Image.new("RGB", (WIDTH, HEIGHT), BLACK)
drawer = ImageDraw.Draw(img)

for i in range(10):
  star = Star.create_random_star(WIDTH, HEIGHT)
  star.draw(drawer)

img.show()