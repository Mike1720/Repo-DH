# index =      0        1       2          3           4           5        6
frutas = ("Manzana", "Uva", "Fresa", "Mandarina", "Aguacate", "Naranja", "Kiwi")
# -index =    -7       -6      -5         -4          -3          -2       -1

for fruta in frutas:
    print(fruta)

for i in range(len(frutas)):
    print(f"{i}: {frutas[i]}")

counter = 0
while counter < len(frutas):
    print(f"Índice {counter}: {frutas[counter]}")
    counter += 1
