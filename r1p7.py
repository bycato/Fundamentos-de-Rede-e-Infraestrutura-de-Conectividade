pre = float(input("Qual o valor de compra do item? "))

if pre < 50:
    valor = pre + (pre * 0.45)
else:
    valor = pre + (pre * 0.30)

print("Valor de aquisição:", pre, "Valor de venda:", valor)