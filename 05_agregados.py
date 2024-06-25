# tuplas = imutáveis
nomes = ("Maria", "João", "Paula")

#lista = mutáveis
notas = [7.8, 8.2, 9.5]
disciplinas = ["Matemática", "Português", "Filosofia"]

disciplinas.append("História")
notas[0] = notas[0] + 1
notas.append(9)

print(f'A nota de {disciplinas[0]} foi {notas[0]}')

print(disciplinas)
print(notas)