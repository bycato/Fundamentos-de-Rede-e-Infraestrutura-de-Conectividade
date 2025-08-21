sal = float(input("Digite o valor do salário: "))
tem = int(input("Digite seu tempo na empresa (em anos): "))

if sal <= 500 and tem < 1: 
    sal = sal + (sal * 0.25)
elif sal <= 1000 and tem < 3:
    sal = sal + (sal * 0.20)
elif sal <= 1500 and tem < 6:
    sal = sal + (sal * 0.15)
elif sal > 2000 and tem > 10:
    print("Sem direito a aumento!")

print(sal)
