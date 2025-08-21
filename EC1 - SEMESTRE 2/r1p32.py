cod = int(input("Digite aqui o código do produto do cardápio: "))
qnt = int(input("Digite aqui a quantidade: "))
nome = ""
preco = 0

if cod == 100:
    nome = "Hot Dog"
    preco = 1.20
elif cod == 101:
    nome = "Bauru"
    preco = 1.30
elif cod == 102:
    nome = "X-Salada"
    preco = 1.50 
elif cod == 103:
    nome = "X-Bacon"
    preco = 1.20
elif cod == 104:
    nome = "X-Burguer"
    preco = 17.00
elif cod == 105:
    nome = "Suco de Laranja"
    preco = 9.50
elif cod == 106:
    nome = "Refrigerante"
    preco = 6.00
else:
    print("Inválido!")

print("Valor do pedido:", preco * qnt,", com", qnt, nome)