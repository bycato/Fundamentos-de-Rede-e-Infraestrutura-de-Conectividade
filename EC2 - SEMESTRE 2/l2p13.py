def calcularTempo(m):
    h = m / 60
    round(h)
    cal = 9
    if h > 1:
        counth = h
        while counth > 1:
            cal = cal + 1.50
            counth = counth - 1 
    elif m < 15:
        cal = 0
    print("Valor:", cal)
    
m = int(input("Digite a quantidade de minutos estacionadas: "))

calcularTempo(m)