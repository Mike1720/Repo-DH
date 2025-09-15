def contador():
    count = 0  # Variable interna que se conserva entre llamadas

    def incrementar():
        nonlocal count  # Permite modificar la variable de la función externa
        count += 1
        return count

    return incrementar


# 1.- "contador()" retorna la función interna "incrementar",
#     la cual recuerda la variable "count" gracias a la clausura.
mi_contador = contador()

# 2.- Cada vez que llamamos a "mi_contador()", se ejecuta "incrementar"
#     y la variable "count" aumenta en 1.
mi_contador()  # count = 1
mi_contador()  # count = 2
mi_contador()  # count = 3
mi_contador()  # count = 4

print(mi_contador())  # Expected output: 5


# Este concepto es algo similar a lo usado en el hook "useState"
# de la libreria de React en JavaScript