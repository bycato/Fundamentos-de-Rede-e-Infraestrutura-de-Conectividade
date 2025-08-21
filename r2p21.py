n = 0
count = 0
soma = 0
while n >= 0 and n <= 10:
    n = int(input("Digite sua nota: "))
    count += 1
    soma += n

media = soma / count
print("Sua média total: ", media)