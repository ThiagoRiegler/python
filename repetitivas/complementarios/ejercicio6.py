n = int(input("Ingrese un numero: "))
aux2 = 0
i = 10

while i <= n:
    aux = n%10
    n = n//10
    aux2 = aux2*10+aux

aux2 = aux2*10+n
print("El numero invertido sera:", aux2)
