cus = float(input("Qual o custo de fabricação? "))

if cus <= 12000:
    dis = cus * 0.05
    imp = 0
elif cus > 12000 and cus <= 25000:
    dis = cus * 0.10
    imp = cus * 0.15
else:
    dis = cus * 0.15
    imp = cus * 0.20

print("Valor final: ", cus + dis + imp)