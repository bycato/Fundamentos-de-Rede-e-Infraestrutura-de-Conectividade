def listaA(lista):
    count = len(lista)
    count1 = len(lista)
    i = 1
    while count > 0:
        print(i , lista[count1 - count])
        count = count - 1
        i = i + 1
        
lista = ["Banana", "Maçã", "Uva"]
listaA(lista)