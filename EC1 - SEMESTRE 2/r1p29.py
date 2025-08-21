est = str(input("Digite a UF: "))
pro = float(input("Digite o valor do produto: "))

if est == "MS":
    imp = pro * 0.08
elif est == "RJ":
    imp = pro * 0.15
elif est == "SP":
    imp = pro * 0.12
elif est == "MG":
    imp = pro * 0.07
else:
    print("UF inválida!")

print("Preço final:", pro + imp, ", sendo de imposto:", imp)
