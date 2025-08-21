n = 1
count = 0
soma = 0
while n > 0:
    n = int(input("Digite sua idade: "))
    soma += n
    count += 1

print("Media: ", soma/count)