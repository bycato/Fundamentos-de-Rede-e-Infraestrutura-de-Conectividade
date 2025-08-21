def menu():
    e = 0
    e = int(input("Escolha a função: \n 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Saída \n"))
    return e

e = menu()
while e <= 5:
    if e == 1:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        soma = n1 + n2 
        print("Soma: ", soma)
        e = int(input("Quer retornar ao menu? \n 1 - Sim \n 2 - Não \n"))
        if e == 1:
            e = menu()
        else:
            exit()
    elif e == 2:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        sub = n1 - n2
        print("Subtração: ", sub)
        e = int(input("Quer retornar ao menu? \n 1 - Sim \n 2 - Não \n"))
        if e == 1:
            e = menu()
        else:
            exit()
    elif e == 3:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        mult = n1 * n2
        print("Multiplicação: ", mult)
        e = int(input("Quer retornar ao menu? \n 1 - Sim \n 2 - Não \n"))
        if e == 1:
            e = menu()
        else:
            exit()
    elif e == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))   
        divi = n1 / n2
        print("Divisão: ", divi)
        e = int(input("Quer retornar ao menu? \n 1 - Sim \n 2 - Não \n"))
        if e == 1:
            e = menu()
        else:
            exit()
    elif e == 5:
        print("Programa terminado.")
        exit()
