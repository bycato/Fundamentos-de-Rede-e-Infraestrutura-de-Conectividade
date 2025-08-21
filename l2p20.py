import random
n = int(input("Quantidade de alunos apresentados: "))
lista = []

def sorteiaAluno(n):
    if n > 0:
        while n > 0:
            nomes = str(input("Nome do aluno:"))
            lista.append(nomes)
            n = n - 1
    print("O aluno a apresentar será: ", random.choice(lista))

sorteiaAluno(n)
    
 