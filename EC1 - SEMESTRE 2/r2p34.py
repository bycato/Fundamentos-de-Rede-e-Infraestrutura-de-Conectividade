n = int(input("Digite um número: "))
if n > 1:
    for i in range(2, n): #dá o stop em 2, e passa como parâmetro o n.
        if n % i == 0: #se a divisão de I não restar nada, não é primo (7/2 por exemplo, resta 1.)
            print("Não é primo.")
            break #dá o break pra não imprimir conforme o for.
        else:
            print("É primo.") 
            break
elif n == 0:
    print("É zero.")
elif n == 1:
    print("É um.")
elif n < 0:
    print("Negativo.")