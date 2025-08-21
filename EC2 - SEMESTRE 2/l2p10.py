def calc(n1, n2, sim): 
    if sim == "+":
        n = n1 + n2
        print(n)
    elif sim == "*":
        n = n1 * n2
        print(n)
    elif sim == "-":
        n = n1 - n2
        print(n)
    elif sim == "/":
        n = n1 / n2
        print(n)
    
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
sim = str(input("Qual o simbolo de operação desejado?"))

calc(n1, n2, sim)