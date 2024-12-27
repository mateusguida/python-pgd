from reportlab.lib import colors
from reportlab.graphics.shapes import (Drawing, Rect, Circle)

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

def draw_profile_picture(drawing: Drawing):
  w = drawing.width
  h = drawing.height
  cx = w // 4
  cy = h // 2
  r = h // 4
  circ_frame = Circle(cx, cy, r, strokeColor=PG_COLORS["green"], fillColor=PG_COLORS["green"])
  drawing.add(circ_frame)
  # TODO: adicionar foto
  # VIDEO = 1:08:06

if __name__ == '__main__':
  
  # cria o espaço
  drawing = Drawing(WIDTH,HEIGHT)

  # desenha o fundo
  draw_background(drawing, (16,16))

  # desenha foto do fã
  draw_profile_picture(drawing)

  #save
  drawing.save(formats=['pdf','png'], outDir=OUT_DIR, fnRoot="carteirinha")