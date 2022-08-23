from operator import truediv


primer = 1
limite = 1000
cont = 0

for i in range(primer, limite):
    primo = True
    j = 2
    while(i > j) & (primo == True):
        if i % j == 0:
            primo = False
        else:
            j = j + 1
    if primo == True:
        print(i, "es primo")
        cont = cont + 1
print("Entre", primer, "y", limite, "hay", cont, "numeros primos")