numero = int(input("1.Ingrese el numero de la tabla de multiplicar que desee: "))
print("Su numero es: ", numero)
M = 1

while numero < 0:
    print("Erro: 1. El numero introducido no puede ser menor que cero.")
    numero = int(input("1.Ingrese el numero de la tabla de multiplicación que desee: "))

while M < 10:

    r = numero * M
    M = M + 1

    print(numero, "x", M -2, "=", r)