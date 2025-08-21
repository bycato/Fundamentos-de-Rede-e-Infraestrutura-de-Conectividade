n1 = int(input("Digite o primeiro valor:"))
n2 = int(input("Digite o segundo valor:"))

ini = min(n1, n2)
fim = max(n1, n2)

soma = 0
mult = 1
impar = False

atual = ini

while atual <= fim:
    if atual % 2 == 0:
        soma += atual
    else:
        mult *= atual
        impar = True
    atual += 1

print("Soma dos pares: ", soma)

if impar:
    print("Multiplicação dos impares: ", mult)
else:
    print("Não tem impares.")