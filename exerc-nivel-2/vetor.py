def magnitude(a, b):
  return ((a**2) + (b**2)) ** (1/2)

def soma_vetor(a,b,c,d):
  return a+c, b+d

def subtr_vetor(a,b,c,d):
  return a-c, b-d

def mult_escalar(a,b,k):
  return a*k, b*k

def prod_escalar(a,b,c,d):
  return a*c + b*d

if __name__ == '__main__':
  # Teste Função Magnitude
  print(magnitude(2,3)) # Resultado = 3,6055
  print(magnitude(-1,2)) # Resultado = 2,2360
  print(magnitude(0,-4)) # Resultado = 4,0
  
  # Teste Função Soma
  x,y = soma_vetor(1,2,3,-1)
  print(f'Vetor resultante é ({x},{y})')  # Resultado = (4,1)
  
  # Teste Função Subtração
  x,y = subtr_vetor(5,4,3,1)
  print(f'Vetor resultante é ({x},{y})')  # Resultado = (2,3)
  
  # Teste Função Multiplicação por Escalar
  x,y = mult_escalar(2,3,4)
  print(f'Vetor resultante é ({x},{y})')  # Resultado = (8,12)
  x,y = mult_escalar(1,-2,-3)
  print(f'Vetor resultante é ({x},{y})')  # Resultado = (-3,6)
  
  # Teste Função Produto Escalar
  x = prod_escalar(2,3,4,-1)
  print(f'O produto escalar é {x}')  # Resultado = 5