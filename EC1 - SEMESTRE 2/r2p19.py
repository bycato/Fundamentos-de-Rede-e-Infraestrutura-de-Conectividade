n = 1
count = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n == 0:
        print("Fim do programa!")
    else:
        if n % 2:
            print(n, "Impar!")
        else:
            print(n, "Par!")
    count = count + 1
    
print("Processos: ", count)