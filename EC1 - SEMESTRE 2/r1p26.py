op = int(input("Digite a sua opção (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão): "))

if op == 1:
    n1 = int(input("Digite seu primeiro número: "))
    n2 = int(input("Digite seu segundo número: "))
    soma = n1 + n2
    print(soma)
    print("Processo finalizado!")
elif op == 2:
    n1 = int(input("Digite seu primeiro número: "))
    n2 = int(input("Digite seu segundo número: "))
    if n1 > n2:
        sub = n1 - n2
    else:
        sub = n2 - n1
    print(sub)
    print("Processo finalizado!")
elif op == 3:
    n1 = int(input("Digite seu primeiro número: "))
    n2 = int(input("Digite seu segundo número: "))
    mult = n1 * n2
    print(mult)
    print("Processo finalizado!")
elif op == 4:
    n1 = int(input("Digite seu numerador: "))
    n2 = int(input("Digite seu denominador: "))
    if n2 > 0:
        div = n1 / n2
        print(div)
    else:
        print("Inválido!")
    print("Processo finalizado!")