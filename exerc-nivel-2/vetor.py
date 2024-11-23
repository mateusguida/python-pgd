# Função para calcular a magnitude de um vetor
def magnitude(vet):
  return ((vet(0)**2) + (vet(1)**2)) ** (1/2)

# Função para somar dois vetores
def somar(v1,v2):
  if len(v1) != len(v2):
    print("Vetores incompatíveis")
    return 0
  res = []
  for i in range(len(v1)):
    res.append(v1[i] + v2[i])
  return tuple(res)

# Função para inverter um vetor
def inverter(v):
  res = []
  for i in range(len(v)):
    res.append(-v[i])
  return tuple(res)

# Função para multiplicar dois vetores
def subtrair(v1,v2):
  return somar(v1, inverter(v2))

def multiplicar(vet,num):
  res = []
  for i in range(len(vet)):
    res.append(vet[i] * num)
  return tuple(res)

# Função que calcula produto escalar entre dois vetores
def prod_escalar(v1,v2):
  if len(v1) != len(v2):
    print("Vetores incompatíveis")
    return None
  soma = 0
  for i in range(len(v1)):
    soma += v1[i] * v2[i]
  return soma

if __name__ == '__main__':
  a = (2,5)
  b = (1.5,7.0)
  num = 4

  print(f'Soma dos vetores {a} e {b}: ', somar(a,b))
  print(f'Diferença dos vetores {a} e {b}: ', subtrair(a,b))
  print(f'Multiplicação de {a} por {num}: ', multiplicar(a,num))
  print(f'Produto escalar entre {a} e {b}: ', prod_escalar(a,b))