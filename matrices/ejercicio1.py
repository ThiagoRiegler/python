a = []
b = []
c = []

print("Ingrese dimension de la matriz, maximo 100")
s = int(input("Numero de filas: "))
r = int(input("Numero de columnas: "))

for i in range(s):
    a.append([])
    b.append([])
    c.append([])
    for j in range(r):
        a[i].append(int(input("A{}{}:".format(i+1,j+1))))
        b[i].append(int(input("B{}{}:".format(i+1,j+1))))
        c[i].append(a[i][j]+b[i][j])

print("Matriz A:",a)
print("Matriz B:",b)
print("Matriz C:",c)
