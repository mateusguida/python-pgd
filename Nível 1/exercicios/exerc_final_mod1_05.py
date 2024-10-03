palavra = input("Digite uma palavra: \n").lower()
letra = input("Digite uma letra: \n").lower()

quant =0

for i in range(len(palavra)):
    if palavra[i]  == letra:
        quant = quant+1

print(f"A palavra {palavra} tem {quant} letras {letra}.")