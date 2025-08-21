def ciVol(h, r):
    cal = 3.141592 * r ** 2 * h
    print("Volume:", cal)
    
h = int(input("Digite a altura:"))
r = int(input("Digite o raio:"))

ciVol(h, r)