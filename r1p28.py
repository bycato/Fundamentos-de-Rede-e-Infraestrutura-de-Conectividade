ano = int(input("Digite um ano:"))

if ano % 400:
    print("Ano bissexto.")
else:
    print("Ano normal.")