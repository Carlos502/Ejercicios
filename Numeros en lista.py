num = int (input("Ingresa un numero: "))
lista = [num]

while num != 0:
    num = int(input("Ingresa un numero: "))

    if num == 0:
        print()

    else:
        lista.append(num)

print(lista)
print("Proceso Finalizado")