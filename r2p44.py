altura1 = 0
idade1 = 0 
peso1 = 0
count = 0
countmasc = 0
countfem = 0
mediaalt = 0
mediaimc = 0
mediamasc = 0
mediafem = 0

for i in range(2):
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite com M ou F seu sexo: "))
    altura = float(input("Digite em metros sua altura: "))
    peso = float(input("Digite em kilos seu peso: "))

    if idade > idade1:
        idade1 = idade

    if altura > altura1:
        altura1 = altura

    if peso > peso1:
        peso1 = peso

    if sexo == "F":
        countfem += 1
    elif sexo == "M":
        countmasc += 1

    mediaalt += altura
    imc = peso / (altura ** 2)
    mediaimc += imc
    count += 1

mediaalt = mediaalt / count
mediaimc = mediaimc / count
mediamasc = (countmasc / count) * 100
mediafem = (countfem / count) * 100
print("Idade da pessoa mais velha: ", idade1)
print("Altura do mais alto: ", altura1)
print("Peso da pessoa mais pesada: ", peso1)
print("Media de Altura: ", mediaalt)
print("Media de IMC: ", mediaimc)
print("Porcentagem de Mulheres: ", mediafem)
print("Porcentagem de Homens: ", mediamasc)