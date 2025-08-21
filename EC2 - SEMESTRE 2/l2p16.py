def calKwh(pot, temp):
    kwh = pot * temp
    print(kwh)

pot = float(input("Digite a potencia do aparelho em kW: "))
temp = float(input("Digite em horas o tempo de uso do aparelho por mês: "))

calKwh(pot, temp)    
    