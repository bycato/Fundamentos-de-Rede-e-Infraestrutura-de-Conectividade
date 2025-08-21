from Estoque import Estoque
class Produto(Estoque): #cria a classe de Produto.
    def __init__(self, nome, desc, preco, estoque): #como não existe estoque sem produto, dá para fazer uma classe pai e filho.
        super().__init__(self, nome, desc, preco) #aproveitando da hereditariedade de funções compartilhadas.
        self.nome = nome
        self.desc = desc
        self.preco = preco
        self.estoque = estoque
        with open("Produtos.txt", "a") as l: #registra, em ordem, os produtos que estão em estoque do sistema.
            l.write(f'{self.nome} | {self.desc} | {self.preco} | {self.estoque} \n')

    def getItem(self): #consulta o produto.
        return self.nome
        
    def getPreco(self): #consulta o preço do produto.
        return self.preco
    
    def getDesc(self): #consulta a descrição do produto.
        return self.desc