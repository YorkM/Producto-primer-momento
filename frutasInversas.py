
frutas = []

for i in range (10):
    fruta = input("Ingrese una fruta: ")
    frutas.append(fruta)
    print(frutas)
    
frutas2 = [fruta for fruta in reversed (frutas)]
print(frutas2)
