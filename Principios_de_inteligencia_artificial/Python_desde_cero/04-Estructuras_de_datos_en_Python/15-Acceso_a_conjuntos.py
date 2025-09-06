conjunto_frutas = {"Manzana", "Pera", "Limón", "Naranja"}

# NO EXISTE EL ACCESO A CONJUNTOS MEDIANTE INDICES
# YA QUE ES UNA COLECCIÓN NO ORDENADA

# ACCESO A CONJUNTO
for fruta in conjunto_frutas:
    if fruta == "Manzana":
        print(fruta)

answer = "Manzana" in conjunto_frutas
print(answer)


# AÑADIR ELEMENTO
conjunto_frutas.add("Fresa")
print(conjunto_frutas)


# AÑADIR OTRO CONJUNTO
nuevo_conjunto = {"Kiwi", "Coco", "Piña"}
# ERROR: conjunto_frutas += nuevo_conjunto -> NO VALIDO
conjunto_frutas.update(nuevo_conjunto)
print(conjunto_frutas)
# Es valido agregar a un conjunto elementos de listas.
lista_frutas = ["Papaya", "Melón", "Platano", "Platano"]
conjunto_frutas.update(lista_frutas)
print(conjunto_frutas)


# ELIMINAR ELEMENTO
# remove -> GENERA ERROR SI NO SE ENCUENTRA EL ELEMENTO A ELIMINAR
conjunto_frutas.remove("Pera")
# discard -> NO GENERA ERROR EN CASO QUE EL ELEMENTO NO SE ENCUENTRE
conjunto_frutas.discard("Platano")
# pop -> ELIMINA EL ULTIMO ELEMENTO QUE SE ENCUENTRE EN ESE MOMENTO AL FINAL DEL SET
conjunto_frutas.pop()
# clear -> ELIMINA TODOS LOS ELEMENTOS DEL CONJUNTO
# conjunto_frutas.clear()
print(conjunto_frutas)

