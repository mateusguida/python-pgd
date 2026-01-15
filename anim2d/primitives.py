import colors

class Quad:
    def __init__(self, coords, pos, speed = 5, color = colors.BLACK):
        self.coords = coords
        self.position = pos
        self.speed = speed
        self.color = color
    
    def __str__(self):
        r = ''
        for i, v in enumerate(self.coords, start=1):
            r += f'v{i}: {v}\n'
        return f"Retângulo\n{r}"
    
    def draw(self, canva, time):
      hside = self.coords[1][0] - self.coords[0][0]
      vside = self.coords[1][1] - self.coords[2][1]
      position = (self.position[0] + time * self.speed[0],
                       self.position[1] + time * self.speed[1])
      for i in range(position[0] - hside//2,
                     position[0] + hside//2):
        for j in range(position[1] - vside//2,
                       position[1] + vside//2):
          canva.putpixel((i,j),self.color)

class Scene:
    def __init__(self, children=[]):
        self.children = children
    
    def add(self, child):
        self.children.append(child)
    
    def draw(self, canva, time):
      for child in self.children:
        child.draw(canva, time)

if __name__ == "__main__":
    square = Quad([(-1, 1), (1, 1), (1, -1), (-1, -1)])
    print(square)