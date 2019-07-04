def factorial(y):
    x = y

    count = 3
    z = 2

    while z <= x:
        count = count * z
        z = z + 1
        print(count)

factorial(6)