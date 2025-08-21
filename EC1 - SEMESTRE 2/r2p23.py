n1 = 3
n2 = 5
soma = 0
for i in range(1000):
    if i % n1 == 0 or i % n2 == 0:
        soma += i
    
print("Soma de múltiplos de 3 ou 5: ", soma)