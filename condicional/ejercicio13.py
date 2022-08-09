ano = int(input("Ingrese el año: "))

if (ano%4==0) & (ano%100!=0) or (ano%400==0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
