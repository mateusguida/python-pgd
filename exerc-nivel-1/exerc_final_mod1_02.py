n = int(input("Digite um número: \n"))

divisores = 0

if n > 1 and n < 10000:
    for i in range(1, n):
        if n%i==0:
            divisores = divisores + 1
else:
    print("Número inválido. Digite um número entre 2 e 9999")

if divisores == 1:
    print(f"O número {n} é um número primo.")
else:
    print(f"O número {n} não é um número primo.")
    