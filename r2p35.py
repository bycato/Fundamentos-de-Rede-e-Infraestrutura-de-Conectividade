def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Digite um valor: "))
soma = 0
count = 0
num = 2

while count < n:
    if primo(num):
        print("Primo: ", num)
        soma += num
        count += 1
    num += 1

print("Soma dos primos: ", soma)