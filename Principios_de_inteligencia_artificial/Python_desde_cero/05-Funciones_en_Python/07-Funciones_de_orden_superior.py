from functools import reduce

# ----------------------------------------
# FUNCIONES DE ORDEN SUPERIOR
# ----------------------------------------


# MAP
# La función map() ejecuta una función especifica por cada elemento en
# un iterable. El elemento es enviado a la función como parametro.

# ITERABLE DE ELEMENTOS
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# FUNCIÓN
def square(number):
    return number * number


cudrado_lista_numeros = list(map(square, lista_numeros))
cubo_lista_numeros = list(map(lambda num: num**3, lista_numeros))
print(cudrado_lista_numeros)
print(cubo_lista_numeros)


# FILTER
# La función filter() retorna un iterador donde los elementos a traves
# de una función para evaluar si el elemento es aceptado o no.


# FUNCIÓN
def impar(num):
    return num % 2 != 0


numeros_pares = list(filter(lambda el: el % 2 == 0, lista_numeros))
numeros_impares = list(filter(impar, lista_numeros))
print(numeros_pares)
print(numeros_impares)


# REDUCE


# FUNCIÓN
def resta(x, y):
    return x - y


sumatoria = reduce(lambda x, y: x + y, lista_numeros)
resta_numeros = reduce(resta, lista_numeros, 100)
print(sumatoria)
print(resta_numeros)
