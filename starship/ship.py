from PIL import ImageDraw

PINK_COLOR = (246, 71, 255)

class Spaceship:
    def __init__(self, x:int, y:int, 
                 width:int, height:int, 
                 speed:int,
                 color:tuple=PINK_COLOR):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

        # para animação estacionária
        self.idle_direction = 1
        self.idle_factor = 0.25
        self.idle_range = 7


    def draw(self, drawer:ImageDraw.ImageDraw):
        top_left_x = self.x - self.width // 2
        top_left_y = self.y - self.height // 2
        bottom_right_x = self.x + self.width // 2
        bottom_right_y = self.y + self.height // 2

        drawer.rectangle((top_left_x, top_left_y, bottom_right_x, bottom_right_y), self.color)

    def idle_target(self, bounds):
        return (bounds[0]//2, bounds[1]//2)

    def update_idle(self, bounds:tuple):
        self.y += (self.speed * self.idle_factor) * self.idle_direction

        target = self.idle_target(bounds)
        if abs(self.y - target[1]) > self.idle_range:
            self.idle_direction = - self.idle_direction

    def update_intro(self, bounds:tuple):
        target_y = bounds[1]//2

        if self.y > target_y:
            self.y -= self.speed

    def update_outro(self, bounds:tuple):
        if self.y + self.height//2 > 0:
            self.y -= self.speed