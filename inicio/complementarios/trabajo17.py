import math

pi = 3.1416

b = float(input("Ingrese el lado b: "))
c = float(input("Ingrese el lado c: "))
alfa = float(input("Ingrese el angulo en grados sexagesimales: "))

a = (b**2 + c**2 - 2*b*c * math.cos(alfa*pi/180))**0.5

print("El valor del lado a es:", a)