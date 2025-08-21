from Cliente import Cliente

class Carrinho(Cliente): #como não existe um carrinho sem um cliente, podemos criar a super classe de um carrinho.
    def __init__(self, nome, idade, cpf): 
        super().__init__(nome, idade, cpf) 
        self.items = [] #lista que armazena os produtos que o cliente escolher colocar no carrinho
        self.preco = [] #lista que armazena os valores dos produtos que foram colocados no carrinho
        
    def addItem(self, newItem): #função que adiciona um item na lista do carrinho.
        newItem.attEstoque() #quando feito, diminui 1 no estoque do produto.
        newItems = newItem.getItem()
        newPreco = newItem.getPreco()
        self.items.append(newItems) #e depois é colocado nas listas em ordem,
        self.preco.append(newPreco) #com o preço e produto separados.
        return print(f'Novo item no carrinho!') #e notifica quando sucedido.

    def remItem(self, newItem): #função que diminui um item na lista do carrinho.
        newItem.devEstoque() #quando feito, aumenta 1 no estoque do produto,
        print(f'Seu Carrinho: {self.items}')
        n = int(input("Deseja retirar o item de qual posição? "))
        del self.items[n] #e faz a deleção do produto no carrinho
        del self.preco[n] #e faz a deleção do valor do produto na soma
        return print(f'Carrinho atual: {self.items}') #e mostra o carrinho atual.

    def getTotal(self): #função que faz a soma de todos os itens na lista de preços separados do carrinho.
        precoTotal = 0
        for i in self.preco:
            precoTotal += i
        return precoTotal #retorna a soma de todos.
    
    def getCarrinho(self): #retorna todos os itens do carrinho, em lista.
        return print(f'{self.items}')
    
    def getCarrinho2(self): #retorna também, porém não é mostrado em print. Serve para o registro em txt.
        return self.items

    def getValor(self): #retorna todos os valores dos itens do carrinho, em lista.
        return print(f'{self.preco}')
    
    def esvaziaCar(self): #esvazia os itens do carrinho.
        self.items.clear()
        self.preco.clear() 
        return print(f'Carrinho está vazio!') #notifica quando sucedido.
    
    def regCompra(self, itens, valor): #registra a compra em txt.
        with open("Compras.txt", "a") as c:
            c.write(f"Itens Comprados: {itens} | Valor da Venda: {valor} \n")
        return print(f'Compra registrada.')