def convS(h, m, s):
    h = h * 3600
    m = m * 60
    s = h + m + s
    print("Segundos: ", s)
    
h = int(input("Digite suas Horas: "))
m = int(input("Digite seus Minutos: "))
s = int(input("Digite seus Segundos: "))

convS(h,m,s)