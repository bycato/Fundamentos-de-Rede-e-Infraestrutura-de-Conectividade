voto = int
ncountj = 0
ncountm = 0
ncounts = 0
ncountjs = 0
ncountn = 0
ncountnb = 0
while voto != 0:
    voto = int(input("Em quem desejas votar? \n 1 - Joao \n 2 - Maria \n 3 - Sarah \n 4 - Jose \n 5 - Nulo \n 6 - Nulo em Branco \n "))
    if voto == 0:
        print("Contagem terminada.")
        break
    elif voto == 1:
        ncountj += 1
    elif voto == 2:
        ncountm += 1
    elif voto == 3:
        ncounts += 1
    elif voto == 4:
        ncountjs += 1
    elif voto == 5:
        ncountn += 1
    elif voto == 6:
        ncountnb += 1

ncounttotal = ncountj + ncountm + ncounts + ncountjs + ncountn + ncountnb
calculo1 = (ncountn/ncounttotal)*100
calculo2 = (ncountnb/ncounttotal)*100

print("Votos no João: ", ncountj)
print("Votos na Maria: ", ncountm)
print("Votos na Sarah: ", ncounts)
print("Votos no José: ", ncountjs)
print("Votos Nulos: ", ncountn)
print("Votos Nulos em Branco: ", ncountnb)

print("Porcentagem Nula sob o total: ", calculo1)
print("Porcentagem Nula em Branco sob o total: ", calculo2)