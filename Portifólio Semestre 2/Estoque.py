class Estoque(): #cria a classe de estoque, podendo fazer a contagem de itens dentro do sistema.
    def __init__(self, nome, desc, preco, estoque): #deve ter as mesmas características do produto para ser herdado.
        self.estoque = estoque 

    def attEstoque(self): #ação acionada quando um produto é processado na compra.
        self.estoque -= 1 #tira um de cada vez.
    
    def devEstoque(self): #ação acionada quando um produto do carrinho é removido.
        self.estoque += 1 #coloca um de cada vez.

    def getEstoque(self): #consulta o estoque.
        return print(f'{self.nome} tem no estoque, {self.estoque} unidades!') #notifica quando sucedido.