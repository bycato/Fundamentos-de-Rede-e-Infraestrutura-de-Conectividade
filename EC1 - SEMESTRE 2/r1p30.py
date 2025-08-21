dis = float(input("Digite a distancia percorrida:"))
lit = float(input("Digite a quantidade consumida:"))

kml = dis / lit

if kml < 8:
    print("Venda o carro.")
elif kml <= 12:
    print("Econômico.")
else:
    print("Super econômico.")
    