def printLista(leng, cont):
    lista = []
    count = leng
    while count > 0:
        lista.append(cont)
        count = count - 1
    print(lista)
        
leng = int(input("Digite o tamanho da lista: "))
cont = str(input("Digite o conteúdo da lista: "))
printLista(leng, cont)