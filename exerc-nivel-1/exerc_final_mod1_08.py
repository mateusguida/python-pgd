caminho = "dois_num.txt"

with open(caminho, 'r', encoding='utf-8') as arq:
    dados = arq.readlines()

caminho = "soma.txt"
with open(caminho, 'w', encoding='utf-8') as arq:
    for p in dados:
        par = p.strip().split(" ")
        soma = int(par[0]) + int(par[1])
        arq.write(str(soma) + "\n")
