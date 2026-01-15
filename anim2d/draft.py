from PIL import Image
import colors

WIDTH = 1000
HEIGHT = 1000

side = 100

cena = Image.new("RGB", (WIDTH, HEIGHT), colors.WHITE)

for i in range(WIDTH//2 - side//2, WIDTH//2 + side//2):
  for j in range(HEIGHT//2 - side//2, HEIGHT//2 + side//2):
    cena.putpixel((i,j),colors.BLACK)

cena.show()