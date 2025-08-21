valor = str(input("Qual seu turno? (M - Matutino, V - Vespertino, N - Noturno): "))

if valor == "M":
    print("Bom dia!")
elif valor == "V":
    print("Boa tarde!")
elif valor == "N":
    print("Boa noite!")
else:
    print("Valor inválido.")
    