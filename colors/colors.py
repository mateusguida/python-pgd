from typing import List
from PIL import Image
import numpy as np

class Color:
    def __init__(self, r:int, g:int, b:int, n:str = ""):
        self.rgb = (r,g,b)
        self.name = n

    def __str__(self):
        return f"{self.name}: RGB{self.rgb}"

    @property # permite utilizar o método como atributo
    def hsv(self):
        r, g, b = self.rgb
        r, g, b = r/255.0, g/255.0, b/255.0
        mx = max(r, g, b)
        mn = min(r, g, b)

        df = mx-mn

        if mx == mn:
            h = 0
        elif mx == r:
            h = (60 * ((g-b)/df) + 360) % 360
        elif mx == g:
            h = (60 * ((b-r)/df) + 120) % 360
        else:
            h = (60 * ((r-g)/df) + 240) % 360
        
        if mx == 0:
            s = 0
        else:
            s = (df/mx)*100
      
        v = mx*100

        return (round(h),round(s),round(v))
  
    def view(self):
        img = Image.new("RGB", (512, 512), self.rgb)
        img.show()

class ColorPalette:
    def __init__(self, name:str, colors: List[Color]):
        self.name = name
        self.colors = colors
    
    def __str__(self):
        text = f"<{self.name}>:\n"
        for i, color in enumerate(self.colors, start=1):
            text += f"  {i}. {color}\n"
        return text
    
    def view(self):
        imgs = []
        for color in self.colors:
            array = np.array(Image.new("RGB", (256, 512), color.rgb))
            imgs.append(array)
        img = Image.fromarray(np.hstack(imgs))
        img.show()

if __name__ == "__main__":
    blue = Color(12,28,52, "azul @pgdinamica")
    green = Color(0,167,150, "verde @pgdinamica")
    print("RGB:", blue.rgb)
    #blue.view()
    print("HSV:", green.hsv)
    #green.view()

    pgpalette = ColorPalette("Paleta P&G Dinâmica", [blue, green, Color(255,255,255,"branco")])
    print(pgpalette)
    pgpalette.view()