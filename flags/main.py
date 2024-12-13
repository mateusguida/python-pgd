import os
from PIL import Image
from cores import VERDE, AMARELO, AZUL, BRANCO
from formas import pintar_losango, pintar_circulo, pintar_faixa

IMG_DIR = "img"
filename = os.path.join(IMG_DIR, "brasil.png")

def bandeira_brasileira(largura):
  M = largura / 14
  comprimento = int(M * 20)

  # pinta toda a área da bandeira de verde
  img = Image.new("RGB", (comprimento,largura), VERDE)

  # calcula os vertices do losango
  dist_vertices = 1.7 * M
  vertices_losango = [
    (dist_vertices, largura/2),
    (comprimento/2, dist_vertices),
    (comprimento - dist_vertices, largura/2),
    (comprimento/2, largura - dist_vertices)
  ]

  # cria e pinta o losango amarelo
  pintar_losango(img, vertices_losango, AMARELO)

  # calculando centro e raio do círculo
  centro = (comprimento // 2, largura // 2)
  raio = 3.5 * M
  
  # cria e pinta o círculo
  pintar_circulo(img, centro, raio, AZUL)

  # calcula centro das faixas
  centro_arcos = (comprimento / 2 - 2 * M, largura - 1)
  rmenor = 8 * M
  rmaior = 8.5 * M

  # cria e pinta faixa
  pintar_faixa(img, centro_arcos, (rmenor, rmaior), (centro, raio), BRANCO)

  return img

if __name__ == '__main__':
  img = bandeira_brasileira(1400)
  img.save(os.path.join(IMG_DIR,"br-passo4.png"))



