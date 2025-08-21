n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

mp = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10

if mp >= 6:
    print("Aprovado, Média:", mp)
elif mp >= 3: 
    print("Exame, Média:", mp)
else:
    print("Reprovado, Média:", mp)

