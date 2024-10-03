caminho = "bimestre.csv"
disciplinas = ["português","matemática","ciências","história","geografia","física"]

with open(caminho, 'w', encoding='utf-8') as arq:
    arq.write("nome,português,matemática,ciências,artes,ed. física\n")

    qtd = int(input("Digite a quantidade de alunos da turma: "))

    for i in range(qtd):
        nome = input("Digite o nome do aluno: ")
        notas = ""
        for d in disciplinas:
            nota = input(f"Digite a nota da disciplina {d}: ")
            notas += "," + nota
        arq.write(nome + notas)