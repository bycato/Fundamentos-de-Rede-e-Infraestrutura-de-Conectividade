def exp(x, y):
    a = 1 #o valor base é um, pois o primeiro sempre é a mesma base.
    for i in range(y): #faz o for na range do expoente
        a *= x #adicionando a multiplicação ao resultado
    return a #retorna o valor total
x = 3
y = 4
print(exp(x, y))
