s = 0
n = int(input("Ingrese el numero de terminos: "))
for x in range(1, n+1):
    if x%2==0:
        s = s-(1/x)
    else:
        s = s+(1/x)

print("La suma sera:", s)
