import random
import math

def calcular_media(dados):
  return sum(dados) / len(dados)

def calcular_desvio_padrao(dados):
  media = calcular_media(dados)
  variancia = sum((x - media)**2 for x in dados) / (len(dados) - 1)
  return math.sqrt(variancia)

caminho = "dados.txt"
quant = 10

for i in range(8):
    vetor = []
    for j in range(quant):
        dado = random.randint(1,6)
        vetor.append(dado)
    media = calcular_media(vetor)
    desvio = calcular_desvio_padrao(vetor)

    with open(caminho, 'a', encoding='utf-8') as arq:
        arq.write("Quantidade: " + str(quant))
        arq.write(", Media: " + str(media))
        arq.write(", Desvio-padrão: " + str(desvio) + "\n")

    quant *= 10
    print(str(12.5 * (i+1)) + "% complete")
print("Análise concluída")

# a partir de 1000 dados gerados, a média e o desvio-padrão são praticamente os mesmos