import random

palavras = ["abacaxi", "banana", "carambola", "damasco", "embauba"]

sorteada = palavras[random.randint(0,4)]
forca = ['-'] * len(sorteada)
erros = 0
acertos = 0

while True:
  chute = input("Escolha uma letra: ")
  pos = 0
  flag = True #começa com verdadeiro, para checar se foi um chute errado
  for letra in sorteada:
    if letra == chute:
      forca[pos] = chute
      acertos += 1
      flag = False #caso pelo menos um chute seja certo, a flag é modificada
    pos += 1

  if(flag):
    erros += 1
  
  if(acertos == len(sorteada)):
    print(f"Parabéns! Você sobreviveu a forca! A palavra era {sorteada.upper()}")
    break
  elif(erros > 5):
    print(f"Eita! Você foi enforcado! A palavra era {sorteada.upper()}")
    break

  print(forca)
