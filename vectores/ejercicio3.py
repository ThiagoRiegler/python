vec = []
n = int(input("Ingrese el numero de elementos en el vector: "))

if 1 <= n and n <= 200:
    for i in range (1, n+1):
        elemento = int(input("Ingrese un entero {0}: ".format(i)))
        vec.append(elemento)

    i=0

    lista_nueva=[]

    for elemento in vec:
        if elemento not in lista_nueva:
            lista_nueva.append(elemento)

    lista_nueva.sort()

print(lista_nueva)
