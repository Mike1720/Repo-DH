# index =      0        1       2          3           4           5        6
frutas = ("Manzana", "Uva", "Fresa", "Mandarina", "Aguacate", "Naranja", "Kiwi")
# -index =    -7       -6      -5         -4          -3          -2       -1

(a, b, c, *d) = frutas

print(a)
print(b)
print(c)
print(d)

# NOTE: NO SE PUEDE DESEMPAQUETAR SOLO UNA PARTE.
# SE PUEDEN DESEMPAQUETAR ELEMENTOS A SUS RESPECTIVAS VARIABLES, PERO
# LAS RESTANTES NECESITAN SER ASIGNADAS A OTRA VARIABLE