import random

palavras = ["abacaxi", "banana", "carambola", "damasco", "embauba"]

sorteada = palavras[random.randint(0,4)]
forca = ['-'] * len(sorteada)
letras = ['-'] * 26
erros = 0
acertos = 0

while True:
  chute = input("Escolha uma letra: ").lower()
  flag = True #começa com verdadeiro, para checar se foi um chute errado

  #checando se a letra já foi escolhida
  asc = ord(chute)-97
  if(letras[asc] == '-'):
    letras[asc] = chute #salvando a letra escolhida
    pos = 0
    # verificando se tem a letra na palavra
    for letra in sorteada:
      if letra == chute:
        forca[pos] = chute
        flag = False
      pos += 1
  else:
    print("Você já chutou essa letra")

  if(flag):
    erros += 1

  print("=============")
  print(forca)
  print("=============")
  print("Letras já escolhidas: ", letras)

  if(erros > 5):
    print(f"Eita! Você foi enforcado! A palavra era {sorteada.upper()}")
    break

  elif(sorteada == ''.join(forca)):
    print(f"Parabéns! Você sobreviveu a forca! A palavra era {sorteada.upper()}")
    break