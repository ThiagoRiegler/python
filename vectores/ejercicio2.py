suma = 0
media = 0.0
c = 0
temp = []

n = int(input("Ingrese la cantidad de temperaturas: "))

for i in range(n):
    temperatura = float(input("Ingrese la temperatura {0}: ".format(i+1)))
    temp.append(temperatura)
    suma = suma + temp[i]

media = suma/n

for temperatura in temp:
    if temperatura >= media:
        c = c + 1
        print(temperatura)

print("La media es", media)
print("Total de temperaturas >= a la media es", c)
