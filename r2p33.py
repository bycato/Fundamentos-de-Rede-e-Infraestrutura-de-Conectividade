media = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
count = 0
for i in range(10):
    n1 = int(input("Digite sua primeira nota: "))
    n2 = int(input("Digite sua segunda nota: "))
    n3 = int(input("Digite sua terceira nota: "))
    n4 = int(input("Digite sua quarta nota: "))

    media = (n1 + n2 + n3 + n4) / 4
    if media >= 7:
        count += 1

print("Número de alunos com média 7 ou acima: ", count)