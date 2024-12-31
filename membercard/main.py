from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
from reportlab.lib import colors
from reportlab.graphics.shapes import (Drawing, Rect, Circle, String)
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont

import json, os

registerFont(TTFont("FiraSans", "assets/FiraSans-Regular.ttf"))
registerFont(TTFont("FiraSans-Bold", "assets/FiraSans-Bold.ttf"))

OUT_DIR = "grafica"
DATA_DIR = "data"
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
  return inner_rect.getBounds()

def draw_profile_frame(drawing: Drawing):
  w = drawing.width
  h = drawing.height
  cx = w // 4
  cy = h // 2
  r = h // 4 + 8
  circ_frame = Circle(cx, cy, r, strokeColor=PG_COLORS["green"], fillColor=PG_COLORS["green"])
  drawing.add(circ_frame)

  return circ_frame.getBounds()

def draw_name_and_username(drawing: Drawing, x, y, margin=(16,32)):
  with open(os.path.join(DATA_DIR, "user.json"), "r") as userfile:
    content = userfile.read()
    user = json.loads(content)
  xmargin = margin[0]
  ymargin = margin[1]
  name = String(x + xmargin, y - ymargin,
                user['name'],
                fontSize=28,
                fontName="FiraSans-Bold",
                fillColor=colors.white,
                strokeColor=colors.white)
  y = name.getBounds()[1]
  username = String(x + xmargin, y - ymargin,
                f"@{user['username']}",
                fontSize=28,
                fontName="FiraSans",
                fillColor=colors.white,
                strokeColor=colors.white)
  y = username.getBounds()[1]

  msg = f"Sou fã de carteirinha do\nProgramação Dinâmica\ndesde {user['subscribed_since']}."
  lines = msg.split("\n")
  texts = []
  for line in lines:
    mul = 0.8 if texts else 1.8
    since = String(x + xmargin, y - int(mul * ymargin),
                  line,
                  fontSize=24,
                  fontName="FiraSans-Bold",
                  fillColor=colors.white,
                  strokeColor=colors.white)
    y = since.getBounds()[1]
    texts.append(since)

  drawing.add(name)
  drawing.add(username)
  for elem in texts:
    drawing.add(elem)

  return texts[-1].getBounds()

def draw_profile_picture(myCanva: canvas.Canvas, framebb, margin = 16):
  myCanva.drawImage("assets/avatar_cropped.png",
                    framebb[0] + margin // 2,
                    framebb[1] + margin // 2,
                    framebb[2] - framebb[0] - margin,
                    framebb[3] - framebb[1] - margin,
                    mask=(0, 1, 0, 1, 0, 1))
  myCanva.drawImage("assets/logo_cropped.png",
                    framebb[2] - 4 * margin,
                    framebb[1],
                    64,
                    64,
                    mask=(0, 1, 0, 1, 0, 1))

if __name__ == '__main__':
  
  myCanva = canvas.Canvas(os.path.join(OUT_DIR, "carteirinha.pdf"), (WIDTH,HEIGHT))

  # cria o espaço
  drawing = Drawing(WIDTH,HEIGHT)

  # desenha o fundo
  draw_background(drawing, (16,16))

  # desenha frame para foto do fã
  bbox = draw_profile_frame(drawing)

  # acrescenta texto
  draw_name_and_username(drawing, bbox[2], bbox[3])

  # acrescenta o desenho da carteirinha e depois a foto do fã
  renderPDF.draw(drawing, myCanva, 0, 0)
  draw_profile_picture(myCanva, bbox)

  # salvamento antigo, usando Drawing - problemas para colocar a foto
  # drawing.save(formats=['pdf','png'], outDir=OUT_DIR, fnRoot="carteirinha")

  # salva pdf
  myCanva.save()

  # mensagem de confirmação
  print("Carteirinha gerada com sucesso!")