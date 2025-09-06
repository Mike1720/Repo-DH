# ------------------------------
# CONJUNTOS (SETS)
# ------------------------------

# Existen valores que pueden ser equivalentes
# True -> 1
# False -> 0
# Por lo que en los conjuntos al ser una colección no ordenada
# y mutable de elementos únicos, no se imprimirán estos valores
# Por lo que se puede decir que estos valores no pueden existir en una
# misma colección

conjunto_frutas = {"Manzana", "Platano", "Pera", 0, False, 1, True}
# Solo imprime 0 y 1, False y True son los 2dos valores "duplicados"
# por lo que no aparecen en la colección.
print(conjunto_frutas)

longitud = len(conjunto_frutas)
print(longitud)

set_constructor = set(("Manzana", "Platano", "Pera", "Pera"))
print(set_constructor)

set_prueba = set(([True]))
print(set_prueba)

# Al igual que las tuplas, al crear un set desde el constructor con un
# tipo de dato diferente al string puede generar error, en caso de ser string
# lo separará y descartará los valores indenticos.
# Para evitar estos errores al tener un solo elemento en tuplas y sets, se debe
# envolver el dato en corchetes, o también se puede añadir una coma (,)
# después del dato.
