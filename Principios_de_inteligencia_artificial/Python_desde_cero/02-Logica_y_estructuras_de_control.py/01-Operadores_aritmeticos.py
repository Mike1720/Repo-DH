# Operadores aritmeticos

# Variables
a = 10
b = 3
c = 2
d = 5
mensaje = ""

# Suma
suma = a + b
mensaje = "El resultado de la suma de {} + {} es: {}".format(a, b, suma)
print(mensaje)

# Resta
resta = d - c
mensaje = "El resultado de la resta de {} - {} es: {}".format(d, c, resta)
print(mensaje)

# Multiplicación
multiplicacion = a * c
mensaje = "El resultado de la multiplicación de {} * {} es: {}".format(
    a, c, multiplicacion
)
print(mensaje)

# División (Cociente)
# Nota: En Python, la división entre enteros produce un resultado de punto flotante
division = a / d
division_entera = a // d  # División entera
mensaje = "El resultado de la división de {} / {} es: {}".format(a, d, division)
print(mensaje)
mensaje = "El resultado de la división de {} / {} es: {}".format(a, d, division_entera)
print(mensaje)

# Módulo (Residuo)
modulo = a % b
mensaje = "El resultado del módulo de {} % {} es: {}".format(a, b, modulo)
print(mensaje)

# Exponente
exponente = c**b
mensaje = "El resultado del exponente de {} ** {} es: {}".format(c, b, exponente)
print(mensaje)

