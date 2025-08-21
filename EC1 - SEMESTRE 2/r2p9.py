c1 = 999999999999999
c2 = -999999999999999
n = 0
while n < 10:
    x = int(input("Digite um número: "))
    if x > c2:
        c2 = x
    if x < c1:
        c1 = x
    n = n + 1

print("Menor: ", c1)
print("Maior: ", c2)