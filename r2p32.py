c = ""
listac = []
count = 0
for i in range(10):
    c = str(input("Digite uma letra: "))
    if c != "a" and c != "e" and c != "i" and c != "o" and c != "u":
        listac.append(c)
        count += 1
    
print("Consoantes: ", listac)
print("Num. Consoantes: ", count)