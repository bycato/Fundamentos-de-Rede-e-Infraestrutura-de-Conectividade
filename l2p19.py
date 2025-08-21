def consumo(km, l):
    gasto = km / l
    if gasto > 15:
        print("Super Econômico!")
    elif gasto < 15 and gasto > 8:
        print("Econômico!")
    else:
        print("Gasta Muito!")

km = int(input("Digite a distancia em km: "))
l = int(input("Digie a quantidade de litros de combustível gasto: "))
consumo(km, l)