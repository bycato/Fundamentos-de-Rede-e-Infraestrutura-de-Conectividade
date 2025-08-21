h = float(input("Digite a altura: "))
sex = str(input("Digite seu sexo: "))

if sex == "M":
    cal = (72.7 * h) - 58
elif sex == "F":
    cal = (62.1 * h) - 44.7

print("Seu peso ideal: ", cal)