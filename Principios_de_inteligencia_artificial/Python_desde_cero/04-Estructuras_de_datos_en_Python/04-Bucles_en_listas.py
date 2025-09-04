# ITERACIÓN SIBRE LISTAS

frutas = ["Manzana", "Platano", "Pera", "Mandarina", "Fresa", "Piña"]


# BUCLE FOR
for fruta in frutas:
    print(fruta)

#                  6
for i in range(len(frutas)):
    print(f"{i}: {frutas[i]}")

# SHORTHAND
[print(f"Fruta actual: {fruta}") for fruta in frutas]


# BUCLE WHILE
j = 0
while j < len(frutas):
    print(frutas[j])
    j += 1
