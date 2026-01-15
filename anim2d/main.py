from PIL import Image
import colors
from primitives import Quad, Scene
import os

OUT_DIR = "runs"

WIDTH = 2000
HEIGHT = 2000

scene = Scene()
sz = 50

square1 = Quad([(-sz, sz),
               (sz, sz),
               (sz, -sz),
               (-sz, -sz)],
               (WIDTH//2, HEIGHT//2), (20,8))

square2 = Quad([(-sz, sz),
               (sz, sz),
               (sz, -sz),
               (-sz, -sz)],
               (WIDTH//2, HEIGHT//2), (-20,0), (255,255,0))

scene.add(square1)
scene.add(square2)

for time in range(30):
  img = Image.new("RGB", (WIDTH, HEIGHT), colors.WHITE)
  scene.draw(img, time)
  img.save(os.path.join(OUT_DIR, f'{time}.png'))