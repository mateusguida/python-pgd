x1 = float(input("Digite a coordenada x do ponto 1: \n"))
y1 = float(input("Digite a coordenada y do ponto 1: \n"))
x2 = float(input("Digite a coordenada x do ponto 2: \n"))
y2 = float(input("Digite a coordenada y do ponto 2: \n"))

dist = ((x1-x2)**2 + (y1-y2)**2) ** (1/2)

print("A distancia é {:.3f}.".format(dist))