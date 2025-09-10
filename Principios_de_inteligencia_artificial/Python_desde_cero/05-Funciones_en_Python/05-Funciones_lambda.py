# FUNCIÓN TÍPICA EJEMPLO 1
def duplicar_numero(n):
    return n * 2


res_func_tipica_1 = duplicar_numero(4)
print(res_func_tipica_1)

# FUNCIÓN LAMBDA (VISUAL) EJEMPLO 1
dup_numero = lambda x: x * 2
res_func_lambda_v_1 = dup_numero(4)
print(res_func_lambda_v_1)


# FUNCIÓN TÍPICA EJEMPLO 2
def multiplicar(x, y):
    return x * y


res_func_tipica_2 = multiplicar(10, 2)
print(res_func_tipica_2)


# FUNCIÓN LAMBDA (VISUAL) EJEMPLO 1
mult = lambda x, y: x * y
res_func_lambda_v_2 = mult(10, 2)
print(res_func_lambda_v_2)


# --------------------------------------------
# FUNCIONES LAMBDA
# --------------------------------------------


def operaciones(tipo_operacion):
    if tipo_operacion.lower() == "suma":
        return lambda x, y: x + y
    elif tipo_operacion.lower() == "resta":
        return lambda x, y: x - y
    elif tipo_operacion.lower() == "multiplicación":
        return lambda x, y: x * y
    else:
        return lambda x, y: x / y


suma = operaciones("suMa")
resta = operaciones("resta")
res_suma = suma(5, 7)
res_resta = resta(5, 7)
print(res_suma)
print(res_resta)

# --------------------------------------------
# EXPLICACIÓN
# --------------------------------------------
# 1.- Se asigna a una variable la función y se le pasa a está su respectivo parametro.
# 2.- Pasado el parametro, se evaluará las condiciones y DEVOLVERÁ una función (función lambda) según el caso,
#     por lo que la variable tendra un valor de función, como en los ejemplos previos.
# 3.- Ahora la variable asignada almacena una función que espera sus respectivos argumentos.
# 4.- La variable ahora devuelve un resultado que debe ser contenido en otra variable para perdurar
#     el resultado


def multiplicador(n):
    return lambda x: x * n


triplicar = multiplicador(3)
duplicar = multiplicador(2)
print(triplicar(5))
print(duplicar(5))
