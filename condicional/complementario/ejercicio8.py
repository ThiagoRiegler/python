from cmath import pi

print("(1: area de triangulo / 2: area de circulo)")
opc = int(input("Ingrese el calculo que desea relaizar: "))

if opc == 1:
    print("Area de triangulo")
    l = float(input("Ingrese el lado del triangulo: "))
    area = ((3**0.5)/4)*l
    print("El area del triangulo es:", area)
elif opc == 2:
    print("Area de circulo")
    r = float(input("Ingrese el radio del circulo: "))
    area = pi * r**2
    print("El area del circulo es:", area)
else:
    print("Error")