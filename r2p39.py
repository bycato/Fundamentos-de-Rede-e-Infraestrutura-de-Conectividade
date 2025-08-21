import random #importa a função random, do próprio python.
n = 0
x = random.randrange(100)
while n != x:
    n = int(input("Faça um palpite: "))
    if n == x:
        print("Você acertou!")
        break
    elif n < x:
        print("O palpite é menor que o número... tente novamente.")
    elif n > x:
        print("O palpite é maior que o número... tente novamente.")