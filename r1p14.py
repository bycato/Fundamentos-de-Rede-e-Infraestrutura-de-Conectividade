n1 = int(input("Digite a nota 1: "))
n2 = int(input("Digite a nota 2: "))

if n1 >= 0 and n1 <= 10 and n2 >= 0 and n2 <= 10:
    media = (n1 + n2) / 2
    print(media)
else:
    print("Inválido.")