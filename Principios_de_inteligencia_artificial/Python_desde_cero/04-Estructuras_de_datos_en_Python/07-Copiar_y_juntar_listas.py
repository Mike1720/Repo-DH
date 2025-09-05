frutas = ["Manzana", "Platano", "Pera"]

copia_frutas = frutas.copy()
copia_frutas2 = list(frutas)

# NO MODIFICA LA LISTA ORIGINAL
copia_frutas[len(copia_frutas) - 1] = "Naranja"
# NO MODIFICA LA LISTA ORIGINAL
copia_frutas2[len(copia_frutas2) - 1] = "Naranja"

frutas2 = ["Mandarina", "Fresa", "Piña"]

# REASIGNAR LA MISMA VARIABLE, ADEMÁS DE AÑADIR OTRA LISTA
#frutas += frutas2
#print(frutas)

# ASGINAR A OTRA VARIABLE LA UNIÓN DE LAS LISTAS
#frutas_conjunto = frutas + frutas2
#print(frutas_conjunto)

frutas.extend(frutas2)
print(frutas)
