from PIL import Image, ImageDraw
import os
from star import Star

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 720
HEIGHT = 1280
NUM_STARS = 50
NUM_FRAMES = 300

def save_gif(frames_dir:str, output_dir:str, exclude:bool=True, fps:int=30):
  filelist = sorted([f for f in os.listdir(frames_dir)
                     if f.endswith(('.png','.jpg','.jpeg'))])
  frames = [Image.open(os.path.join(frames_dir, name))
            for name in filelist]
  frames[0].save(os.path.join(output_dir, "universo.gif"),
                 save_all=True,
                 append_images=frames[1:],
                 duration=1/fps,
                 loop=0)
  if exclude:
    print("Excluindo arquivos temporários...")
    for f in filelist:
      os.remove(os.path.join(frames_dir, f))

def main(output_dir:str):
  if not os.path.exists(output_dir):
    os.makedirs(output_dir,exist_ok=True)

  stars = [Star.create_random_star(WIDTH, HEIGHT)
           for i in range(NUM_STARS)]
  
  for frame_idx in range(NUM_FRAMES):
    bounds = (WIDTH, HEIGHT)
    img = Image.new("RGB", (WIDTH, HEIGHT), BLACK)
    drawer = ImageDraw.Draw(img)
    for star in stars:
      star.draw(drawer)
      star.update_position(bounds)
    img.save(os.path.join(output_dir, f"{frame_idx:04d}.png"))

  print("Animação finalizada. Salvando GIF...")
  gifs_dir = "runs/gifs"
  save_gif(output_dir, gifs_dir)
  print("GIF salvo em {gifs_dir}")

if __name__ == "__main__":
  output_dir = "runs/frames"
  main(output_dir)