menor = 999999999999999999999
maior = 1
n = 0
while n >= 0:
    n = int(input("Digite um número: ")) 
    if n > maior:
        maior = n
    elif n < menor and n > 0:
        menor = n

print("Maior:", maior)
print("Menor:", menor)