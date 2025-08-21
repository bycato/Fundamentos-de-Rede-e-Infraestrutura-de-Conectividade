lista = []
lpar = []
limp = []

for i in range(20):
    n = int(input("Digite um valor: "))
    lista.append(n)
    if n % 2 == 0:
        lpar.append(n)
    else:
        limp.append(n)

print("Valores digitados: ", lista)
print("Valores pares: ", lpar)
print("Valores impares: ", limp)