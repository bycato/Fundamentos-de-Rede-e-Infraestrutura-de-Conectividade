a = int(input("Digite A:"))
b = int(input("Digite B:"))
c = int(input("Digite C:"))

if a > 0:
    r1 = (-b + (b ** 2 - 4 * a * c)) / 2 * a
    r2 = (-b - (b ** 2 - 4 * a * c)) / 2 * a
    print("Raiz I: ", r1, "\n Raiz II: ", r2)
elif a == 0:
    r1 = (-b + (b ** 2 - 4 * a * c)) / 2 * a
    print("Raiz única.", r1)
else:
    print("Não é equação de segundo grau.") 