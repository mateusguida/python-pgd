from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, Rect

OUT_DIR = "grafica"
WIDTH = 640
HEIGHT = 360

PG_COLORS = {
  "blue": colors.HexColor("#062846"),
  "green": colors.HexColor("#109395")
}

def draw_background(drawing,
                    margin = (16,16),
                    radius = 64):
  outer_rect = Rect(0, 0, WIDTH, HEIGHT,
            fillColor = PG_COLORS["green"])
  drawing.add(outer_rect)

  xmargin = margin[0]
  ymargin = margin[1]

  inner_rect = Rect(xmargin,
                    ymargin,
                    WIDTH - xmargin*2,
                    HEIGHT - ymargin*2,
                    radius, radius,
                    fillColor = PG_COLORS["blue"],
                    strokeColor = PG_COLORS["blue"])
  drawing.add(inner_rect)

if __name__ == '__main__':
  
  # cria o espaço
  drawing = Drawing(WIDTH,HEIGHT)

  # desenha o fundo
  draw_background(drawing, (16,16))

  #save
  drawing.save(formats=['pdf','png'], outDir=OUT_DIR, fnRoot="carteirinha")