# STRINGS (Cadena de carácteres)

# ----------------
# Tipos de comillas
# ----------------
txt1 = "Hola mundo"
txt2 = 'Hola mundo'
txt3 = """Hola 
mundo""" # Triple comillas para cadenas multilínea

print(txt1)
print(txt2)
print(txt3)


# ----------------
# Index
# ----------------
txt = "Hola mundo"
print(txt[0]) # H
print(txt[1]) # o
print(txt[2]) # l
print(txt[3]) # a
print(txt[4]) # (muestra el espacio)


# ----------------
# length
# ----------------
lenTxt1 = "Mike MV"
lenTxt2 = """Aprendiendo
Python 
en
Digital House"""
longitudTexto1 = len(lenTxt1)
longitudTexto2 = len(lenTxt2)

print(longitudTexto1) # 7
print(longitudTexto2) # 36


# ----------------
# in y not in
# ----------------
txt4 = "Aprendiendo un nuevo lenguaje de programación"
isIn1 = "nuevo" in txt4
isIn2 = "ción" in txt4
isNotIn1 = "Java" not in txt4
isNotIn2 = "lenguaje" not in txt4
print(isIn1) # True
print(isIn2) # True
print(isNotIn1) # True
print(isNotIn2) # False


# ----------------
# slicing
# ----------------
# i     0123456789012345678901234567890
txt5 = "Seguimos trabajando con strings"
slicedText1 = txt5[9:19] 
slicedText2 = txt5[9]
slicedText3 = txt5[:10]
slicedText4 = txt5[10:]
slicedText5 = txt5[::2]
slicedText6 = txt5[-4:]
slicedText7 = txt5[-12:-1]
print(slicedText1) # trabajando
print(slicedText2) # t
print(slicedText3) # Seguimos t
print(slicedText4) # rabajando con strings
print(slicedText5) # Sgios rabjn o tig
print(slicedText6) # ings
print(slicedText7) #  con string


# ----------------
# lower() y upper()
# ----------------
txt6 = "ESCRIBIR EN MAYUSCULAS APARENTA QUE ESTAS GRITANDO"
txtLower = txt6.lower()
print(txtLower)

txt7 = "escribir en minusculas hace que nadie te preste atención"
txtUpper = txt7.upper()
print(txtUpper)


# ----------------
# strip()
# ----------------
txt8 = "          hay demasiados espacios en blanco alrededor      "
txtStripped = txt8.strip()
print(txtStripped)


# ----------------
# Concatenación
# ----------------
a = "Hola"
b = "mundo"
c = a + " " + b
print(c) # Hola mundo

newText = "El contenido de este curso va a durar: "
duration = 10

# Solución 1
#fullText = newText + duration # Error: son 2 tipos de datos diferentes, se necesita castear
fullText = newText + str(duration)
print(fullText)

# Solución 2
fullText2 = f"{newText}{duration}"
print(fullText2)

# Opción 2
newText2 = "El contenido de este curso va a durar: {} y tendrá {} clases"
newText3 = "El contenido de este curso va a durar: {1} y tendrá {0} clases"
duration2 = 15
clases = 20
fullText3 = newText2.format(duration2, clases)
fullText4 = newText3.format(clases, duration2)
print(fullText3)
print(fullText4)


# ----------------
# Escape de caracteres
# ----------------
texto1 = "La mejor serie de mi vida es \"Arcane\""
texto2 = 'La mejor serie de mi vida es "Arcane"'
texto3 = "La mejor serie de mi vida es: \n\"Arcane\"" # \n salto de línea
print(texto1)
print(texto3)


# ----------------
# Métodos de strings
# ----------------
#       |         |         |         |         |         |         |         |         |         |         |
# i     01234567890123456789012345678901234567890123456789012345678901234567890
base = "texto de ejemplo para probar diferentes métodos de strings desde python"

# ----------------
# capitalize(): Capitaliza la primer letra de la cadena
baseCapitalized = base.capitalize() 
print(baseCapitalized)

# ----------------
# title(): Capitaliza la primer letra de cada palabra dentro de la cadena
baseTitle = base.title()
print(baseTitle)

# ----------------
# center(): Centra el texto en un espacio de largo definido
word = "Centrado"
wordCentered = word.center(20)
print(wordCentered)

# ----------------
# count(searchedValue, start, end): Cuenta la cantidad de veces que aparece un valor dentro de la cadena
numRepetitions = base.count("de") # 4, "desde" tambien lo toma en cuenta
print(numRepetitions)

# ----------------
# endswith(value): Devuelve True si la cadena termina con el valor indicado
endsWith = base.endswith("python")
print(endsWith)

# ----------------
# find(value, start, end): Busca un valor dentro de la cadena y devuelve la posición de la primer coincidencia. Si no lo encuentra devuelve -1
isFound1 = base.find("métodos")
isFound2 = base.find("java")
print(isFound1)
print(isFound2)

# ----------------
# isdigit(): Devuelve True si la cadena es un número
num1 = "12345"
num2 = "12345abc"
isNum1 = num1.isdigit()
isNum2 = num2.isdigit()
print(isNum1)
print(isNum2)
# ----------------