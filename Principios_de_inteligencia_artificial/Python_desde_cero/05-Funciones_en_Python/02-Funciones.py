def mostrar_mercaderia(mercaderia):
    for item in mercaderia:
        print(item)


lista_frutas = ["Manzana", "Plarano", "Durazno", "Piña"]
mostrar_mercaderia(lista_frutas)


def division(a, b):
    return a / b


# POSITIONAL ARGUMENT
# ARGUMENTOS PASADOS CONFORME SU POSICIÓN
print(division(1, 2))


def division2(a, b):
    return a / b


# KEYWORD ARGUMENT
# ARGUMENTOS IDENTIFICADOS EN BASE AL KEYWORD DEL PARAMETRO
print(division2(b=2, a=1))


# **KWARGS
# MÉTODO PARA RECIBIR COMO PARAMETRO UN DICCIONARIO.
# LOS ARGUMENTOS SE PASAN COMO ELEMENTOS KEY-VALUE
def division3(**numeros):
    #      nameDic["key"]/nameDic["key"]
    return numeros["a"] / numeros["b"]


#               K-V  K-V
print(division3(b=3, a=1))


# *Args
# MÉTODO PARA RECIBIR COMO PARAMETRO UNA TUPLA.
def division4(*numeros):
    return numeros[0] / numeros[1]


print(division4(1, 2))


def operaciones(a, b):
    suma = a + b
    resta = a - b
    division = a / b
    multiplicacion = a * b

    retornar = {
        "suma": suma,
        "resta": resta,
        "división": division,
        "multiplicación": multiplicacion,
    }

    return retornar


resultados_4_2 = operaciones(4, 2)
print(resultados_4_2)
