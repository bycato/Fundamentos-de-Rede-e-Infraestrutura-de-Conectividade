def revNum(n):
    rev = 0
    while n > 0:
        div = n % 10 #divide por 10 para poder chegar na posição do numero
        rev = rev * 10 + div #rev guarda o numero e imprime o prox em seguida
        n = n // 10 
    print(rev)

n = int(input("Digite um número: "))

revNum(n)