edad = int(input("¿Cuántos años tienes?: "))

if edad >= 18:
    print("Eres mayor de edad")

elif edad <= 0:
    print("Error, ingrese edad correcta")

elif edad < 18:
    print("Eres menor de edad")
