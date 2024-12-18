from PIL import Image
from cores import VERDE, AMARELO, AZUL_BR, AZUL_FR, BRANCO, VERMELHO_JP, VERMELHO_GR, VERMELHO_FR, DOURADO, PRETO
from formas import pintar_losango, pintar_circulo, pintar_faixa, pintar_faixa_hor, pintar_faixa_vert

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
  pintar_circulo(img, centro, raio, AZUL_BR)

  # calcula centro das faixas
  centro_arcos = (comprimento / 2 - 2 * M, largura - 1)
  rmenor = 8 * M
  rmaior = 8.5 * M

  # cria e pinta faixa
  pintar_faixa(img, centro_arcos, (rmenor, rmaior), (centro, raio), BRANCO)

  return img, 'brasil.png'



def bandeira_japao(largura):
  M = largura / 3
  comprimento = int(M * 2)

  # pinta toda a área da bandeira de branco
  img = Image.new("RGB", (largura, comprimento), BRANCO)

  # calculando centro e raio do círculo
  centro = (comprimento // 2, largura // 2)
  raio = 3.5 * M
 
  # cria e pinta o círculo
  pintar_circulo(img, centro, raio, VERMELHO_JP)

  return img, 'japao.png'


def bandeira_alemanha(largura):
  M = largura / 3
  comprimento = int(M * 2)

  # pinta toda a área da bandeira de preto
  img = Image.new("RGB", (largura, comprimento), PRETO)

  # cria e pinta as faixas horizontais
  pintar_faixa_hor(img, VERMELHO_GR, DOURADO)

  return img, 'alemanha.png'

def bandeira_franca(largura):
  M = largura / 3
  comprimento = int(M * 2)

  # pinta toda a área da bandeira de preto
  img = Image.new("RGB", (largura, comprimento), BRANCO)

  # cria e pinta as faixas verticais
  pintar_faixa_vert(img, AZUL_FR, VERMELHO_FR)

  return img, 'franca.png'