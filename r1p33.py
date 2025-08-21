antigo = float(input("Digite o valor antigo:"))

if antigo <= 50:
    antigo = antigo + (antigo * 0.05)
    print(antigo)
elif antigo > 50 and antigo <= 100:
    antigo = antigo + (antigo * 0.10)
    print(antigo)
elif antigo > 100:
    antigo = antigo + (antigo * 0.15)
    print(antigo)

print("Programa finalizado!")