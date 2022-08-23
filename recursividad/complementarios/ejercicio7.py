n = int(input("Ingrese un numero: "))
con = 0

for i in range(2, n):
    if n%i==0:
        con = con+1

if con == 0:
    print(n, "es un numero primo")
else:
    print(n, "no es un numero primo")
    