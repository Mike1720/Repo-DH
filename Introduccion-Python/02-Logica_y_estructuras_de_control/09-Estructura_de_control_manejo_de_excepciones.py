# Estructura de control Manejo de excepciones
# Las excepciones son errores que ocurren durante la ejecución de un programa.
# En Python, podemos manejar estas excepciones utilizando las estructuras try, except y finally.
# La estructura try se utiliza para envolver el código que podría generar una excepción.
# La estructura except se utiliza para manejar la excepción si ocurre.
# La estructura finally se utiliza para ejecutar código que siempre debe ejecutarse, independientemente de si ocurrió una excepción o no.

# Ejemplo: Manejo de división por cero

a = 10
b = 2
result = 0

# ------------------------------------
# ERROR
# c = a / b # Esto generará un error de división por cero
# print(c)
# ------------------------------------

try:
    # try envuelve el código que podría generar una excepción
    result = a // b
    print(f"El resultado de la división de {a} entre {b} es: {result}")
except ZeroDivisionError:
    # except captura la excepción específica de división por cero
    print("Error: No se puede dividir por cero.")
finally:
    # finally se ejecuta siempre, nos permite limpiar recursos, cerrar archivos, etc.
    result = 0 

print(result) # El resultado es 0 porque la división fue exitosa y no se generó una excepción
