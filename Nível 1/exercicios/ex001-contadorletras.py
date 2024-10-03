palavra = input("Digite uma palavra ")
letra = input("Digite uma letra ")
contador = 0

p = 0
posicao = []

for c in palavra:
  if c == letra:
    contador += 1
    posicao.append(p)
  p += 1

print(contador)
print(posicao)
