# RECURSIÓN
# Es una técnica donde una función se llama a si misma dentro, algo
# parecido a lo que son los bucles.


def suma_naturales(numero):
    if numero == 1:
        return 1
    else:
        return numero + suma_naturales(numero - 1)


def comprobacion(numero):
    acumulador = 0
    for i in range(1, numero + 1):
        acumulador += i
    return acumulador


print(suma_naturales(5))
print(comprobacion(5))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(6))


def contador(n, lim):
    print(n)
    n += 1
    if n <= lim:
        contador(n, lim)


contador(1, 10)
