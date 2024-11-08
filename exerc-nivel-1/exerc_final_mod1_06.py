palavra = input("Digite uma palavra: \n").lower()
letra = input("Digite uma letra: \n").lower()

quant = 0
lista = []

for i in range(len(palavra)):
    if palavra[i]  == letra:
        quant = quant+1
        lista.append(i)

print(f"A palavra {palavra} tem {quant} letras {letra}.")

if len(lista) != 0:
  print(f"A letra {letra} está nas posições {lista} da palavra {palavra}")