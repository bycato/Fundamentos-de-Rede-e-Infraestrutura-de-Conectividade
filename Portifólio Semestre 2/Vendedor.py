class Vendedor: #classe onde as pessoas podem ser identificadas ao colocar anúncios para vender.
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        with open("Vendedores.txt", "a") as l: #todos os vendedores terão seus dados guardados após ser instanciados.
            l.write(f'{self.nome} | {self.email} \n')

    def realVenda(self): #tem o poder de realizar a venda e finalizar a compra.
        return print(f'Venda realizada! Obrigado por comprar!') 
    
    def cadastrarVend(self): #função que atualiza o cadastro do vendedor (antes era nulo, agora contém os dados inputados).
        newName = input("Digite seu nome: ")
        newEmail = input("Digite seu email: ")
        self.nome = newName
        self.email = newEmail

        