r1 = 1
r2 = 1
while r1 != 0 or r2 != 0:
    r1 = int(input("Insira a resistencia 1: "))
    if r1 == 0:
        print("Fim do programa.")
        break
    r2 = int(input("Insira a resistencia 2: "))
    if r2 == 0:
        print("Fim do programa.")
        break
    a = (r1 * r2) / (r1 + r2)
    print("Associação em paralelo: ", a)