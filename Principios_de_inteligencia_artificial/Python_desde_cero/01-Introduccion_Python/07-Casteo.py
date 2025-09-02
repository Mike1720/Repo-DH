# TEXTO (str)
variable1 = "Texto" # class str
variable2 = "12345" # class str
variable3 = "Texto12345" # class str

# NUMERICO (int, float, complex)
variable4 = 10 # class int
variable5 = 2.5 # class float
variable6 = 1j # class complex

# LISTA (list)
variable7 = [1, 3, 5, 7] # class list

#  TUPLA (tuple)
variable8 = (1, 2, 4, 8) # class tuple

# Impresión de las variables y sus tipos
print(variable1)
print(type(variable1))
print(variable2)
print(type(variable2))
print(variable3)
print(type(variable3))
print(variable4)
print(type(variable4))
print(variable5)
print(type(variable5))
print(variable6)
print(type(variable6))
print(variable7)
print(type(variable7))
print(variable8)
print(type(variable8))

# CASTEO (Conversión de tipos de datos)
# Convertir str a int 
#casteo_str_int1 = int(variable1) # ERROR: no se puede convertir un texto a un número
casteo_str_int2 = int(variable2) # Convierte valores númericos en texto a int
#casteo_str_int3 = int(variable3) # ERROR: no se puede convertir un texto a un número

# Convertir int a str
casteo_int_str1 = str(variable4) # Convierte un número entero a texto
casteo_int_str2 = str(variable5) # Convierte un número decimal a texto
casteo_int_str3 = str(variable6) # Convierte un número complejo a texto

# Convertir list a tuple
casteo_list_tuple = tuple(variable7)

# Convertir tuple a list
casteo_tuple_list = list(variable8)


print("----------- CASTEO -----------")
print("          STR a INT           ")
print(casteo_str_int2)
print(type(casteo_str_int2))
print("          INT a STR           ")
print(casteo_int_str1)
print(type(casteo_int_str1))
print(casteo_int_str2)
print(type(casteo_int_str2))
print(casteo_int_str3)
print(type(casteo_int_str3))
print("          LIST a TUPLE        ")
print(casteo_list_tuple)
print(type(casteo_list_tuple))
print("          TUPLE a LIST        ")
print(casteo_tuple_list)
print(type(casteo_tuple_list))