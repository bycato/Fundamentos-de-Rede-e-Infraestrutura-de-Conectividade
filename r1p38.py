dh = float(input("Quanto você ganha por hora?"))
nh = float(input("Quanto você trabalhou em horas?"))

ir = (dh * nh) * 0.11
inss = (dh * nh) * 0.08
sind = (dh * nh) * 0.05

print("Salário bruto:", dh * nh)
print("Salário liq: ", (dh * nh) - inss - ir - sind)