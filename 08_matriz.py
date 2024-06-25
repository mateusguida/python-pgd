lin = int(input("Digite a quantidade de linhas da matriz "))
col = int(input("Digite a quantidade de colunas da matriz "))

matriz = []

for l in range(lin):
  vetor = []
  for c in range(col):
    vetor.append(input(f"Digite o elemento [{l+1}][{c+1}] da matriz: "))
  matriz.append(vetor)

print("------")
for l in range(lin):
  print("| ", end="")
  for c in range(col):
    print(f"{matriz[l][c]} | ", end="")
  print("\n--------")