a = int(input("Ingrese el año: "))
m = int(input("Ingrese el mes: "))
d = int(input("Ingrese el dia: "))

if d>0 and d<30:
    print("Mañana es",d+1,m,a)
else: 
    if m>0 and m<12:
        print("Mañana es",1,m+1,a)
    else:
        print("Mañana es",1,1,a+1)
