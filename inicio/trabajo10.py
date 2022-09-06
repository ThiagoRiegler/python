radio = float(input("Ingrese el radio: "))
altura = float(input("Ingrese la altura: "))
pi = 3.1416

vol = pi * radio**2 * altura
area = 2 * pi * radio * (altura+radio)

print("El volumen del cilindro es:", vol)
print("El area del cilindro es:", area)