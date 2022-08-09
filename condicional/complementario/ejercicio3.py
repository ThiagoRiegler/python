precio = float(input("Ingrese el precio del articulo: "))
marca = input("Ingrese la marca del articulo: ")

if precio>=2000:
    precio = precio*0.9
if marca=="NOSY":
    precio = precio*0.95

print("El total es:", precio*1.2)
