# Operadores de asginación
# Los operadores de asignación se utilizan para asignar valores a las variables.

# Operador igual (=)
x = 5

# Operador suma y asignación (+=)
x += 3 # Equivalente a: x = x + 3, x = 8
x += 3 # Equivalente a: x = x + 3, x = 11
x += 3 # Equivalente a: x = x + 3, x = 14
print(x) # output: 14

# Operador resta y asignación (-=)
x -= 2 # Equivalente a: x = x - 2, 14 - 2 = 12
x -= 2 # Equivalente a: x = x - 2, 12 - 2 = 10
x -= 2 # Equivalente a: x = x - 2, 10 - 2 = 8
print(x) # output: 8

# Operador multiplicación y asignación (*=)
x *= 4 # Equivalente a: x = x * 4, 8 * 4 = 32
x *= 4 # Equivalente a: x = x * 4, 32 * 4 = 128
print(x) # output: 128

# Operador división y asignación (//=)
x //= 2 # Equivalente a: x = x // 2, 128 / 2 = 64
print(x) # output: 64
# En caso de requerir una división con punto flotante se utiliza /=

# Operador exponenciación y asignación (**=)
x **= 2 # Equivalente a: x = x ** 2, 64 ** 2 = 4096
print(x) # output: 4096

# Operador módulo y asignación (%=)
x %= 1000 # Equivalente a: x = x % 1000, 4096 % 1000 = 96
print(x) # output: 96