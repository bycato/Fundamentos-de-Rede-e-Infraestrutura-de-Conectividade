def maior(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print("O maior: ", n1)
    elif n2 > n1 and n2 > n3:
        print("O maior: ", n2)
    elif n3 > n1 and n3 > n2:
        print("O maior: ", n3)
    
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

maior(n1, n2, n3)