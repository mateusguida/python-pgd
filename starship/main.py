import os
from PIL import Image, ImageDraw
from star import Star
from ship import Spaceship

BLACK = (0, 0, 0)
WIDTH = 720
HEIGHT = 1280
NUM_STARS = 50
# NUM_FRAMES = 150
MAX_FRAMES = 300

def save_gif(frames_dir, 
            filepath, 
            exclude=True,
            fps=30):
    filelist = sorted([f for f in os.listdir(frames_dir) 
                if f.endswith(('png', 'jpg', 'jpeg'))])

    frames = [Image.open(os.path.join(frames_dir, name)) 
              for name in filelist]
    frames[0].save(
        filepath,
        save_all=True,
        append_images=frames[1:],
        duration=1/fps,  # 500 milliseconds per frame
        loop=0  # Loop indefinitely
    )
    if exclude:
        print("Excluindo frames originais")
        for filename in filelist:
            os.remove(os.path.join(frames_dir, filename))


def is_visible(ship: Spaceship, bounds) -> bool:
    left = ship.x - ship.width//2
    right = ship.x + ship.width//2
    top = ship.y - ship.height//2
    bottom = ship.y + ship.height//2

    horizontal = right > 0 and left < bounds[0]
    vertical = bottom > 0 and top < bounds[1]
    return horizontal and vertical


def generate_animation(ship: Spaceship, idle_duration_frames=90):
    frames = []
    stars = [Star.create_random_star(WIDTH, HEIGHT) 
             for i in range(NUM_STARS)]
    
    bounds = (WIDTH, HEIGHT)
    # for frame_idx in range(NUM_FRAMES):
    animation = 'intro'
    print("Animação de entrada")
    idle_frames = 0
    frame_idx = 0
    while animation != 'done' and frame_idx < MAX_FRAMES:
        img = Image.new("RGB", bounds, BLACK)
        drawer = ImageDraw.Draw(img)
        for star in stars:
            star.draw(drawer)
            star.update_position(bounds)
        
        if animation == 'intro':
            ship.update_intro(bounds)
            if (ship.y - ship.idle_target(bounds)[1]) < ship.idle_range:
                animation = 'idle'
                print("Mudando para animação de repouso")
        elif animation == 'idle':
            ship.update_idle(bounds)
            idle_frames += 1
            if idle_frames >= idle_duration_frames:
                animation = 'outro'
                print("Mudando para animação de saída")
        elif animation == 'outro':
            ship.update_outro(bounds)
            if not is_visible(ship, bounds):
                animation = 'done'
                print("Animação finalizada!")

        ship.draw(drawer)
        frame_idx += 1
        frames.append(img)
    return frames


def main(output_dir:str, filename):
    if not os.path.exists(outdir_dir):
        os.makedirs(outdir_dir, exist_ok=True)

    ship = Spaceship(WIDTH//2, HEIGHT, 60, 90, 7)
    frames = generate_animation(ship)

    [img.save(os.path.join(output_dir, f"{idx:04d}.png")) 
     for idx, img in enumerate(frames)]
    print("Gerando gif...")
    gifpath = os.path.join("runs", "gifs", filename)
    save_gif(output_dir, gifpath, exclude=False)
    print(f"Gif salvo em {gifpath}")

if __name__ == '__main__':
    outdir_dir = "runs/frames"
    filename = "HallShip-v3.gif"
    main(outdir_dir, filename)