idade = int(input("Digite sua idade: \n"))
analfabeto = int(input("Você é analfabeto? Digite [1] para sim e [2] para não: \n"))

if analfabeto == 1:
  analfabeto = True
else:
  analfabeto = False

if (idade >16 and idade<18) or idade>70 or analfabeto:
    print("O seu voto é facultativo!")
elif idade < 16:
    print("Você é proibido de votar!")
else:
    print("Você é obrigado a votar!")