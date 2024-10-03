a = float(input("Digite o lado a do triângulo: \n"))
b = float(input("Digite o lado b do triângulo: \n"))
c = float(input("Digite o lado c do triângulo: \n"))

if (a < 0) or (b < 0) or (c < 0):
  print("Valor inválido. Digite somente números não negativos")
else:
  if (a < b + c) and (b < a + c) and (c < a + b):
    print("É triângulo")
  else:
    print("Não é triângulo")