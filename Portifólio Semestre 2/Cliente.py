class Cliente: #cria a classe Cliente.
    
    def __init__(self, nome, idade, cpf): #atributos da classe.
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def Cadastrar(self): #registra o cliente recém cadasatrado no arquivo txt.
        with open("Clientes.txt", "a") as file:
            file.write(f'{self.convertStr()} \n')
        return True
    
    def convertStr(self): #função feita para converter os dados em string, assim conseguindo converter em txt.
        return f'{self.nome}, {self.idade}, {self.cpf}'
    
    def getNome(self): #retorna o nome,
        return self.nome
    
    def getCpf(self): #retorna o cpf,
        return self.cpf
    
    def getIdade(self): #e retorna a idade.
        return self.idade