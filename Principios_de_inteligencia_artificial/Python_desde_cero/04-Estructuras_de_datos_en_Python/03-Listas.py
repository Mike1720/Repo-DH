# ------------------------------
# LISTAS
# ------------------------------

# index     0          1        2        3         4
lista = ["Manzana", "Banana", "Pera", "Manzana", "Kiwi"]
# index     -5         -4       -3       -2        -1
print(
    f"""
      Elementos de la lista:{lista}
"""
)

# ACCEDER A ELEMENTOS DE LA LISTA
print(lista)
# Accede al ultimo elemento de la lista
print(lista[-1])
# Accede al cuarto elemento de la lista
print(lista[3])
# Accede a una porción de la lista (desde el elemento en el índice 1 hasta el índice 4, sin incluir este último)
print(lista[1:4])
# Accede a una porción de la lista (desde el inicio hasta el índice 4, sin incluir este último)
print(lista[:4])
# Accede a una porción de la lista (desde el indice 2 hasta el final)
print(lista[-3:-2])

# VERIFICAR SI UN ELEMENTO ESTÁ EN LA LISTA
is_in_list = "Pera" in lista
print(is_in_list)

# MODIFICAR ELEMENTOS DE LA LISTA
lista[-1] = "Sandia"
lista[1:3] = ["Uva", "Melón"]
print(
    f"""
    Elementos de la lista modificada: {lista}
"""
)

# INSERTAR ELEMENTOS EN LA LISTA
# Inserta "Cereza" en la posición 1
lista.insert(1, "Cereza")
# Agrega "Naranja" al final de la lista
lista.append("Naranja")
print(
    f"""
    lista con elementos agregados: {lista}
"""
)

# UNIR OTRA LISTA
# Es posible unir tanto listas como tuplas a otra lista base
tupla = ["Ciruela", "Toronja", "Papaya"]
lista.extend(tupla)
print(
    f"""
    lista unida con tupla: {lista}
"""
)


# ELIMINAR UN ELEMENTO ESPECIFICO
lista.remove("Ciruela")
print(
    f"""
    lista con elementos removidos: {lista}
"""
)

# ELIMINAR POR ÍNDICE
lista.pop(2)
lista.pop()
print(
    f"""
    lista con elementos removidos2: {lista}
"""
)

# LIMPIEZA DE LISTA
#lista.clear()