n = 1
raiz = 0
quadrado = 0
cubo = 0
while n > 0:
    n = int(input("Insira um valor: "))
    if n <= 0:
        print("Fim do programa.")
        break
    raiz = n ** 0.5
    quadrado = n ** 2
    cubo = n ** 3
    print("Sua raiz: ", raiz)
    print("O quadrado: ", quadrado)
    print("O cubo: ", cubo)