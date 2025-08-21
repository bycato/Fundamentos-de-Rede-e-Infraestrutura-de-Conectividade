i = int(input("Quantos números você quer digitar?"))
c = 0
menor = 99999999999999
while c < i:
    n = int(input("Digite um número:"))
    c = c + 1
    if n < menor:
        menor = n

print(menor)