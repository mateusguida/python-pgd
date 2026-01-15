import random

STAR_COLOR = (255, 255, 255)  # Yellow color for the star
STAR_SIZES = (1,2,3)
STAR_SPEEDS = (1,2,3)

class Star:

  def __init__(self, center, size, speed, color):
    self.x = center[0]
    self.y = center[1]
    self.size = size
    self.speed = speed
    self.color = color

  def create_random_star(xmax, ymax, color=STAR_COLOR):
    x = random.randint(0, xmax)
    y = random.randint(0, ymax)
    size = random.choice(STAR_SIZES)
    speed = random.choice(STAR_SPEEDS)
    return Star((x, y), size, speed, color)
  
  def draw(self, drawer):
    # A estrela usa o 'desenhista' externo para se desenhar
    center = (self.x, self.y)
    drawer.circle(center, self.size, self.color)

  def update_position(self, bounds):
    self.y += self.speed
    if self.y > bounds[1]:
      self.y = 0
      self.x = random.randint(0, bounds[0])