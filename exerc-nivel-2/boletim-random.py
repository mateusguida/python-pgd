import random

def cria_boletim(caminho, separador, aluno):
    with open(caminho, 'w', encoding='utf-8') as arq:
        arq.write("Boletim - " + aluno + "\n")
        arq.write("Disciplina" + separador + "Nota\n")
        for i in range(len(disciplinas)):
            arq.write(disciplinas[i] + separador + str(notas[i]) + "\n")

disciplinas = ("Matemática", "Português", "Filosofia", "História", "Física", "Geografia", "Química", "Biologia")

notas = []
for i in range(len(disciplinas)):
    nota = round(random.uniform(0.0,10.0),1)
    notas.append(nota)

nome = input("Digite o nome do aluno: ")
cria_boletim("bimestre.txt", " - ", nome)
cria_boletim("bimestre.csv", ",", nome)

print("Boletim - " + nome)
print("===========================")
for i in range(len(disciplinas)):
    print(f"A nota da {disciplinas[i]} foi {notas[i]}")