lim = int(input("Ingrese la cantidad de numeros a comparar: "))
n = int(input("Ingrese un numero: "))

men = n
may = n

for i in range(1, lim):
    n = int(input("Ingrese otro numero: "))

    if n < men:
        men = n
    elif n > may:
        may = n
    
print("El numero menor es:", men)
print("El numero mayor es:", may)
