val = float(input("Qual o valor de venda? "))

if val > 100000:
    com = 700 + (val * 0.16)
    print(com)
elif val < 100000 and val >= 80000:
    com = 650 + (val * 0.14)
    print(com)
elif val < 80000 and val >= 60000:
    com = 600 + (val * 0.14)
    print(com)
elif val < 60000 and val >= 40000:
    com = 550 + (val * 0.14)
    print(com)
elif val < 40000 and val >= 20000:
    com = 500 + (val * 0.14)
    print(com)
else:
    com = 400 + (val * 0.14)
    print(com)