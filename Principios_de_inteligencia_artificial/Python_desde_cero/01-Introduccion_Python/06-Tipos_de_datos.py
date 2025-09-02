# TIPOS DE DATOS

# TEXTO
# str (cadena de carácteres)
texto = "Hola mundo"

# NUMERICOS
# int (entero)
numero_entero = 20
# float (decimal)
numero_decimal = 20.5
# complex (complejo)
numero_complejo = 2 + 3j

# SECUENCIALES
# list (lista) colección ordenada y mutable
lista = [1, 2, 3, 4]
# tuple (tupla) colección ordenada e inmatable
tupla = (1, 2, 3, 4)
# range (rango) colección de números enteros inmutable
rango = range(10) # Crea un rango de números enteros de 0 a 9

# MAPAS
# dict (diccionario) colección no ordenada de pares clave-valor
diccionario = {
    "nombre": "Miguel",
    "edad": 34,
    "ciudad": "CDMX"
}

# SET
# set (conjunto) colección no ordenada y mutable de ELEMENTOS ÚNICOS ¡No se permiten duplicados!
conjunto = {1, 2, 3, 4}
# frozenset (conjunto inmutable) conjunto inmutable de ELEMENTOS ÚNICOS
conjunto_inmutable = frozenset({1, 2, 3, 4})

# BOOLEANO
# boolean (booleano) tipo de dato que puede ser True o False
booleano_true = True
booleano_false = False

# BINARIO
# bytes (bytes) Representa una secuencia inmutable de bytes
bytes_data = b"datos en bytes"
# bytearray (bytearray) Representa una secuencia mutable de bytes
bytearray_data = bytearray(b"datos en bytearray")
# memoryview (vista de memoria) Permite acceder a los objetos de bytes sin copiarlos.
memoria = memoryview(b"datos en memoria")

# NULO
# NoneType (nulo) Representa la ausencia de valor
nulo = None

