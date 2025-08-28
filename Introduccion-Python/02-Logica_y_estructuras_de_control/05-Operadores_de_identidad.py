# Operadores de identidad
# Los operadores de identidad son "is" e "is not". Estos operadores se utilizan para comparar la identidad de dos objetos, es decir, si ambos objetos son el mismo objeto en memoria.

# Operador "is"
a = [1, 2, 3]
b = a
c = [1, 2, 3]
d = 5
e = 5
print(a is b) # True porque b es una referencia al mismo objeto que a
print(a is c) # False porque c es un objeto diferente aunque tenga el mismo contenido
print(d is e) # True porque los enteros pequeños son internamente referenciados al mismo objeto

# Operador "is not"
print(a is not b) # False porque b es una referencia al mismo objeto que a
print(a is not c) # True porque c es un objeto diferente aunque tenga el mismo contenido
print(d is not e) # False porque los enteros pequeños son internamente referenciados al mismo objeto
