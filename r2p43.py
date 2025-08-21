maior = 0
menor = 20
lista = []
for i in range(7):
    n = int(input("Insira o valor da sua nota: "))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    lista.append(n)
    
lista.sort()
lista.remove(maior)
lista.remove(menor)

media = sum(lista) / 5

print("Resultado Final: ")
print("Maior nota: ", maior)
print("Menor nota: ", menor)
print("Media: ", media)