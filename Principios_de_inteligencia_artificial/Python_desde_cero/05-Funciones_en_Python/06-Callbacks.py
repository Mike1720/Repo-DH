# FUNCIONES COMO ARGUMENTOS
def aplicar_func(func, valor):
    return func(valor)


def cuadrado(x):
    return x * x


def cubo(x):
    return x * x * x


sqr = aplicar_func(cuadrado, 4)
cb = aplicar_func(cubo, 4)

print(sqr)
print(cb)
