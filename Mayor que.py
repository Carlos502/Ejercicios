print("Que numero es mayor")

n1 = float(input("Ingrese el 1er numero: "))
n2 = float(input("Ingrese el 2do numero: "))

if n1 > n2:
    print(n1, "Es mayor que", n2)

elif n1 < n2:
    print(n2, "Es mayor que", n1)

elif n1 == n2:
    print(n2, "Es igual que", n1)