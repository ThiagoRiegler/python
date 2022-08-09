num = int(input("Ingrese un numero entre 0 y 10: "))

if num < 0 or num > 10:
    print("El numero esta fuera del rango")
elif num%2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
