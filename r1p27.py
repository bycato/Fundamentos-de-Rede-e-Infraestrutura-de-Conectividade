idade = int(input("Insira sua idade: "))
tempo = int(input("Insira seus anos trabalhados: "))

if idade > 65 or tempo > 30:
    print("Pode se aposentar.")
elif idade > 60 and tempo > 25:
    print("Pode se aposentar.")
else:
    print("Ainda não.")
