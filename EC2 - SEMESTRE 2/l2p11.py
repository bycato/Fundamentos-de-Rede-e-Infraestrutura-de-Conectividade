def sal(h, v):
    sal = h * v 
    if h > 40:
        sal = (sal * 0.5) + sal
    print("Salário: ", sal)
        
h = int(input("Quantidade de horas trabalhadas:"))
v = float(input("Valor das horas:"))

sal(h, v)
