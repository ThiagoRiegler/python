i = 1
c = 0
numEntradas = 10

print("Ingrese", numEntradas, "numeros:")
while i <= numEntradas:
    n = int(input("Ingrese un numero: "))
    if n%2 == 0:
        c = c+1

    i = i+1

print("En", numEntradas, "numeros enteros hay", c, "numeros pares")
