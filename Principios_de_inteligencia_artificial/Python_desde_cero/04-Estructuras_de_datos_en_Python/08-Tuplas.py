# ------------------------------
# TUPLAS
# ------------------------------
# Una tupla debe tener al menos un elemento y debe contener una coma (,)
# ya que en caso de tener solo un elemento, se considera como string
frutas = ("Manzana", "Platano", "Cereza", "Manzana")
numeros = (1, 2, 3, 4, 5, 5, 1)
mixto = (1, "string", True)

print(frutas)
print(type(frutas))
print(numeros)
print(type(numeros))

tupla_ejemplo = tuple((1, 2, 3, 4, "string", False))
print(tupla_ejemplo)

# CUIDADO: EN CASO DE TENER UN SOLO ELEMENTO AÑADIDO AL CONSTRUCTOR TUPLA
# PUEDE GENERAR UN ERROR, EN EL CASO DE BOOLEANOS, INT, ETC., O SEPARAR LOS CARACTERES
# EN EL CASO DE STRING
tupla_ejemplo2 = tuple((3))
print(tupla_ejemplo2)
