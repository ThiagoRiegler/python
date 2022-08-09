num = float(input("Ingrese un numero: "))
x = int(input("Ingrese la operacion a realizar: "))

funcion = {
    1: 100*num,
    2: 100**num,
    3: 100/num
}

val = funcion.get(x, 0)

print("El resultado es:", val)
