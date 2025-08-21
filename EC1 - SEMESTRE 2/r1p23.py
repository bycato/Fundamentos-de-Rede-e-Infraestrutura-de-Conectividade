bma = float(input("Digite o valor da Base Maior: "))
bme = float(input("Digite o valor da Base Menor: "))
h = float(input("Digite o valor da Altura: "))

cal = ((bma + bme) * h) / 2

if bma > 0 and bme > 0:
    print("Área do trapézio: ", cal)
else:
    print("Inválido.")