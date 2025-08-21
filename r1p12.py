n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print(n1, "é maior que", n2, "e a diferença é:", n1 - n2)
elif n1 == n2:
    print("Os dois são iguais.")
else:
    print(n2, "é maior que", n1, "e a diferença é:", n2 - n1)
