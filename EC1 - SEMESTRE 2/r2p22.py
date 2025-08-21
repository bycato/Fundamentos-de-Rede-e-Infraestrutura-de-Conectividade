def divisores(n):
    for i in range(1, n//2+1): # faz o for, onde começaria por 1, e daria divisão redondada pra cada for
        if n % i == 0:
            yield i #distribui o valor da variável sem pausar a função
    yield n #distribui o valor final

n = 625 #valor inicial
print(list(divisores(n))) #chamada da função, imprime os valores que o YIELD trás em lista, dando append em cada loop.