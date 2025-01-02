from PIL import Image
import os

IMG_DIR = "data/"

# Este código contém um bug
def limit_img_size(img:Image, limit=1024):
    width, height = img.size
    if min(width, height) < limit:
        limit = min(width, height)
    left = (width - limit) // 2
    top = (height - limit) // 2
    right = (width + limit) // 2
    bottom = (height + limit) // 2
    # Corta o centro da imagem
    img = img.crop((left, top, right, bottom))
    return img

if __name__ == '__main__':
    img = Image.open(os.path.join(IMG_DIR, "teste.jpg"))
    cutted = limit_img_size(img)
    cutted.save(os.path.join(IMG_DIR, "cutted.png"))