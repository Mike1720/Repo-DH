# ORDENAMIENTO DE LISTAS

frutas = ["Manzana", "Platano", "Pera", "Mandarina", "Fresa", "Piña"]
frutas2 = ["manzana", "Platano", "Pera", "Mandarina", "fresa", "Piña"]
numeros = [9, 999, 88, 1, 2, 3]

# Ordena las frutas en orden alfabetico en orden ascendente (a-z)
# frutas.sort()
# Ordena las frutas en orden alfabetico en orden ascendente aún cuando hay mayúsculas y minúsculas
frutas2.sort(key=str.lower)
# Ordena los números en orden descendente (+∞,-∞)
numeros.sort(reverse=True)
# Invierte el orden de posicionamiento de la lista
frutas.reverse()

print(frutas)
print(frutas2)
print(numeros)
