n1 = int(input("Digite o início do intervalo: "))
n2 = int(input("Digite o final do intervalo: "))

if n1 > n2:
    print("Valor inválido.")
    exit()
else:
    i = n1
    soma = 0
    if i % 2 == 0:
        soma = i + 1
    for _ in range(n1,n2):
        soma += i
        i += 2
        if i > n2:
            break
        print(soma)
        print(i)
    
print("Soma dos impares do intervalo: ", soma)