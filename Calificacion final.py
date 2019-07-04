nota = int(input("¿Cuánto sacaste en tu nota final?: "))

if nota <= 0:
    print("Error, ingrese calificacion correcta")

elif nota < 5:
    print("Suspenso")

elif nota == 8:
    print("Suficiente")

elif nota == 6:
    print("Aprobado")

elif nota == 7:
    print("Notable")

elif nota > 10:
    print("Error, ingrese calificacion correcta")

elif nota >= 8:
    print("Sobresaliente")