cap = float(input("Ingrese el capital: "))
interes = int(input("Ingrese el interes: "))
anos = int(input("Ingrese los años: "))
j = 1

while (cap < 0) or (interes <= 0) or (interes >= 100) or (anos <= 0):
    print("Ingrese el capital, el interes y el tiempo apropiados")
    cap = float(input("Ingrese el capital: "))
    interes = int(input("Ingrese el interes: "))
    anos = int(input("Ingrese los años: "))

for j in range(anos):
    cap = cap*(1+interes/100)

print("Tienes", cap, "soles")