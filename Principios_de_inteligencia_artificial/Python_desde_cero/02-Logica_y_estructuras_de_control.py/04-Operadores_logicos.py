# Operadores logicos
# AND, OR, NOT

# Variables
a = 5 == 5  # True
b = 3 > 1  # True
c = 2 < 1  # False
d = 4 != 4  # False

print(
    """Valores de las variables:
      a = {}
      b = {}
      c = {}
      d = {}
""".format(
        a, b, c, d
    )
)

# AND -> Devuelve True si AMBOS operandos son True
print("Operador lógico AND:")
print(a and b)  # Ambos son True -> True
print(a and c)  # Uno de ellos es False -> False
print(c and d)  # Ambos son False -> False

# OR -> Devuelve True si AL MENOS UNO de los operandos es True
print("Operador lógico OR:")
print(a or b)  # Ambos son True -> True
print(a or c)  # Uno de ellos es True -> True
print(c or d)  # Ambos son False -> False

# NOT -> Invierte el valor del operando
print("Operador lógico NOT:")
print(not a) # a es True -> not convierte a False
print(not c) # c es False -> not convierte a True