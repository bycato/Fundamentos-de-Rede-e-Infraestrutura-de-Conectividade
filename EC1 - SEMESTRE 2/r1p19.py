n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

mp = ((n1 * 1) + (n2 * 1) + (n3 * 2)) / 4

if mp >= 6:
    print("Aprovado. Média:", mp)
else:
    print("Reprovado.", mp)