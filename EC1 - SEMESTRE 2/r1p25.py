a = float(input("Digite o valor do primeiro lado:"))
b = float(input("Digite o valor do segundo lado:"))
c = float(input("Digite o valor do terceiro lado:"))

if a == b and b == c:
    print("Triângulo equilátero.")
elif a == b or b == c:
    print("Triângulo isósceles.")
elif a != b and b != c:
    print("Triângulo escaleno.")
    