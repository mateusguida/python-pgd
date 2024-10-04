import triangulos as tri

op = input("Digite 1 se deseja inserir os lados do triângulo ou 2 se deseja inserir as coordenadas de seus vérticas: ")

# enquanto uma opção válida não for digitada, o programa repetirá o pedido

while (op != '1') and (op != '2'):
  print("\nOpção inválida. Tente novamente.\n")
  op = input("Digite 1 se deseja inserir os lados do triângulo ou 2 se deseja inserir as coordenadas de seus vérticas: ")

# se a opção for 1, já recebe diretamente o valor dos lados

if op == '1':
  a = float(input("\nDigite um valor de lado: "))
  b = float(input("Digite um valor de lado: "))
  c = float(input("Digite um valor de lado: "))

# se a opção for 2, calcula os lados a partir dos vértices

elif op == '2':
  x = []
  y = []
  print()
  for i in range(3):
    x1 = float(input(f"Digite a coordenada x do vértice {i+1}: "))
    y1 = float(input(f"Digite a coordenada y do vértice {i+1}: "))
    x.append(x1)
    y.append(y1)

  a = tri.calcula_lados(x[0], y[0], x[1], y[1])
  b = tri.calcula_lados(x[0], y[0], x[2], y[2])
  c = tri.calcula_lados(x[1], y[1], x[2], y[2])

# validando triângulo para gerar perímetro e área

if tri.triangulo_valido(a, b, c):
  perimetro = tri.perimetro(a,b,c)
  print(f"\nO perímetro do triângulo de lados {a:.3f}, {b:.3f} e {c:.3f} é {perimetro:.3f}")
  area = tri.area(a,b,c)
  print(f"A área do triângulo de lados {a:.3f}, {b:.3f} e {c:.3f} é {area:.3f}\n")
else:
  print(f"{a}, {b} e {c} NÃO formam um triângulo VÁLIDO!")