filas = 6

for i in range(filas):
    for j in range(filas - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

# Espacios
# primera_vez = 6 - 0 - 1 = 5
# segunda_vez = 6 - 1 - 1 = 4
# tercera_vez = 6 - 2 - 1 = 3
# cuarta_vez  = 6 - 3 - 1 = 2
# quinta_vez  = 6 - 4 - 1 = 1
# sexta_vez   = 6 - 5 - 1 = 0

# Asteriscos
# primera_vez = 2 * 0 + 1 = 1
# segunda_vez = 2 * 1 + 1 = 3
# tercera_vez = 2 * 2 + 1 = 5
# cuarta_vez  = 2 * 3 + 1 = 7
# quinta_vez  = 2 * 4 + 1 = 9
# sexta_vez   = 2 * 5 + 1 = 11