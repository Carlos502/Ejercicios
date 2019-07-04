numero = int(input("Introduzca un numero: "))

while numero < 1:
    print("El numero introducido no puede ser menor que 1.")
    numero = int(input("Introduzca un numero: "))

if numero == 3:
    print(nuero)
else:
    for i in range (2, numero):
        esprimo = True
        for j in range (3,i):
            if i % j == 0:
                esprimo = False
        if esprimo is True:
            print("Es primo: ", i)