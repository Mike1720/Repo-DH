# index =      0        1       2          3           4           5        6
frutas = ("Manzana", "Uva", "Fresa", "Mandarina", "Aguacate", "Naranja", "Kiwi")
# -index =    -7       -6      -5         -4          -3          -2       -1

# GENERÁ ERROR
# frutas[1] = "Coco"
# print(frutas)


# MODIFICACIÓN DE ELEMENTO DE UNA TUPLA
# 1.- Creación de lista en base a una tupla
# frutas_support = list(frutas)
# 2.- Modificación de elemento en la lista
# frutas_support[1] = "Coco"
# 3.- Casteo de lista previa (lista -> tupla), y asignación de esta a la variable inicial de la tupla original
# frutas = tuple(frutas_support)


# AÑADIR ELEMENTO AL FINAL DE LA TUPLA
# 1.- Creación de lista en base a tupla
# frutas_support = list(frutas)
# 2.- Metodo append de las listas para agregar elemento al final de la lista
# frutas_support.append("Frambuesa")
# 3.- Casteo de lista previa (lista -> tupla), y asignación de esta a la variable inicial de la tupla original
# frutas = tuple(frutas_support)

# UNIÓN DE TUPLAS
# frutas2 = ("Coco", "Frambuesa")
# frutas += frutas2


# ELIMINAR ELEMENTO DE TUPLA
# 1.- Creación de lista en base a tupla
# frutas_support = list(frutas)
# Método remove de las listas para eleminar elemento específico de la lista
# frutas_support.remove("Aguacate")
# 3.- Casteo de lista previa (lista -> tupla), y asignación de esta a la variable inicial de la tupla original
# frutas = tuple(frutas_support)

print(frutas)
