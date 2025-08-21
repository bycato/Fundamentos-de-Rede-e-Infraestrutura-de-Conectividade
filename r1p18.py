n = int(input("Digite um número: "))
soma = 0
while n > 0: #verifica se o número é maior que 0 
    n, d = divmod(n, 10) #divide o valor em casas numericas (centenas, dezenas) e separa os numeros que estão na posição em cada while
    soma += d #adiciona na variável o valor da posição até a unidade
print(soma) #printa o resultado