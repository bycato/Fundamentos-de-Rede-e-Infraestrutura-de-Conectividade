n = 0
x = 0
c = 0

while n < 10:
    c = int(input("Digite um numero: "))
    if c > 0:
        x = c + x
    n = n + 1
    
x = x / 10
print("Média:", x)