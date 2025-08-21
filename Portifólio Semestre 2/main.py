from Cliente import Cliente
from Carrinho import Carrinho
from Produto import Produto
from Vendedor import Vendedor

print("Bem vindo! Escolha sua opção:")
n = int(input("1 - Cadastro | 2 - Compra |  3 - Sair")) #sistema de seleção por terminal
if n > 0: #verifica se o número é valido
    while n != 3: #enquanto o usuário não escolhe sair, o sistema é reiniciado toda vez que terminar a ação.
        
        if n == 1: #se escolheu o cadastro,
            c = int(input("1 - Cliente | 2 - Vendedor")) #pergunta quem vai ser cadastrado
            if c == 1: #verifica quem foi selecionado

                usu1 = Cliente("","","")
                usu1.nome = input("Digite seu nome: ")
                usu1.idade = input("Digite sua idade: ")
                usu1.cpf = input("Digite seu cpf: ")
                cadastro = usu1.Cadastrar() #após os dados preenchidos, a variável é atualizada com os dados novos.

                if cadastro == True: #verifica se o cadastro deu certo.
                    print("Usuário cadastrado! Eba!!")
                else:
                    print("Erro ao cadastrar!!")

            elif c == 2:#verifica quem foi selecionado
                vend = Vendedor("", "") 
                vend.nome = input("Digite seu nome: ")
                vend.email = input("Digite seu email: ")
                cadastro = vend.cadastrarVend()
            else: #se não for um cadastro válido
                exit() #o programa fecha.

        elif n == 2: #se foi escolhida a opção de Compra,
            vend = Vendedor("", "")
            prd1 = Produto("Tenis", "Nike Casual", 100, 10) #Os produtos carregam
            prd2 = Produto("Calça", "Calça Adidas", 40, 15)
            prd3 = Produto("Sapato", "Adidas Casual", 100, 20)

            #o Carrinho é designado para aquele usuário
            carrinho = Carrinho(usu1.getNome(), usu1.getIdade(), usu1.getCpf())
            carrinho.getCarrinho()

            carrinho.addItem(prd1) #os itens podem ser adicionados um por um
            carrinho.getCarrinho()

            carrinho.addItem(prd2)
            carrinho.getCarrinho()

            carrinho.addItem(prd3)
            carrinho.getCarrinho()

            #carrinho.remItem(prd1) #ou removidos um por um

            valor = carrinho.getTotal() #os valores são somados um por um no carrinho

            vend.realVenda() #e a venda é realizada,

            with open("Compras.txt", "a") as c: #e registrada em TXT.
                c.write(f"Itens Comprados: {carrinho.getCarrinho2()} | Valor da Venda: {carrinho.getTotal()} \n")    

        n = int(input("1 - Cadastro | 2 - Compra | 3 - Sair")) #depois de realizar a venda, aparecerá a tela novamente.
elif n > 3: #se o número não for válido, o programa fecha.
    exit()
else: #se o número não for válido, o programa fecha.
    exit()