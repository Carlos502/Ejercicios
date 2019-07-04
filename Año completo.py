print("1.Enero, 2.Febrero, 3.Marzo, 4.Abril, 5.Mayo, 6.Junio, 7.Julio, 8.Agosto, 9.Septiembre, 10.Octubre, 11.Noviembre, 12.Diciembre")

Mes = ["Error","Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

numero = int(input("Ingrese un numero: "))

print(Mes[numero])


if numero <= 0:
    print("Ingrese un numero entre 1 y 12")
    numero = int(input("Ingrese un numero: "))

if numero > 8:
    print("Error, Ingrese un numero entre 1 y 12")
    numero = int(input("Ingrese un numero: "))