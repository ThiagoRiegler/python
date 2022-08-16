num = int(input("Ingrese un numero, y para acabar uno negativo: "))

while num > 0:
    suma = 0
    for i in range(1,num+1):
        if num % i == 0:
            suma = suma+i
    print("La suma de los divisores del numero es:", suma)
    num = int(input("numero: "))
