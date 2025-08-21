n = 0
soma = 0
count = 1
for i in range(5):
    n = int(input("Digite um número: "))
    soma += n
    if count == 1:
        n1 = n
    elif count == 2:
        n2 = n
    elif count == 3:
        n3 = n
    elif count == 4:
        n4 = n
    elif count == 5:
        n5 = n
    count += 1

print(soma)
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)