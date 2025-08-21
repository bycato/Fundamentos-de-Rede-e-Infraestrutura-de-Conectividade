n = int(input("Digite um numero entre 100 e 9999: "))
count = 0

if n >= 100 and n <= 9999:
    for a in str(n):  #transforma o número em string, e percorre por cada caractere.
        print(a)
else:
    print("Digito incorreto.")
    
