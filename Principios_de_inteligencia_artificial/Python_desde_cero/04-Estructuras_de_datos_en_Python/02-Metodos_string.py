# MÉTODOS DE STRINGS

texto1 = "hola mundo"
texto2 = "HOLA MUNDO"
texto3 = "   Python es genial   "
texto4 = "Python, React, JavaScript"
texto5 = "12345"
texto6 = "     "
texto7 = "Manzana, Naranja, Manzana, Pera, Uva"
lista = ["Python", "React", "JavaScript"]

print(
    f"""
    texto1: {texto1}
    texto2: {texto2}
    texto3: {texto3}
    texto4: {texto4}
    texto5: {texto5}
    texto6: {texto6}
    lista: {lista}
"""
)

# capitalize: Retorna una copia del string con el primer carácter en mayúscula y el resto en minúscula
print(f"capitalize en texto1: {texto1.capitalize()}")

# upper: Retorna una copia del string con todos los caracteres en mayúscula
print(f"upper en texto1: {texto1.upper()}")

# lower: Retorna una copia del string con todos los caracteres en minúscula
print(f"lower en texto2: {texto2.lower()}")

# strip: Elimina los espacios en blanco al inicio y al final del string
print(f"strip en texto3: {texto3.strip()}")

# replace: Reemplaza todas las ocurrencias de una subcadena por otra
print(f"replace en texto1: {texto1.replace("mundo", "Python")}")

# split: Divide el string en una lista usando el separador especificado
print(f"split en texto4: {texto4.split(", ")}")

# join: Une los elementos de una lista en un string usando el separador especificado
print(f"join en lista: {", ".join(lista)}")

# index: Busca una subcadena y devuelve su posición o lanza un error si no la encuentra
print(f"index en texto1: {texto1.index("mundo")}")

# find: Busca una subcadena y devuelve su posición o -1 si no la encuentra
print(f"find en texto1: {texto1.find("mundo")}")

# rfind: Busca una subcadena desde el final y devuelve su posición o -1 si no la encuentra
print(f"rfind en texto7: {texto7.rfind("Manzana")}")

# startswith: Verifica si el string comienza con la subcadena especificada
print(f"startswith en texto1: {texto1.startswith("hola")}")

# endswith: Verifica si el string termina con la subcadena especificada
print(f"endswith en texto4: {texto4.endswith("Script")}")

# isdigit: Verifica si el string contiene solo digitos (True/False)
print(f"isdigit en texto5: {texto5.isdigit()}")

# isalpha: Verifica si el string contiene solo letras, sin caracteres especiales ni espacios (True/False)
print(f"isalpha en texto1: {texto1.isalpha()}")

# isalnum: Verifica si el string contiene solo letras y/o números, sin caracteres especiales ni espacios (True/False)
print(f"isalnum en texto5: {texto5.isalnum()}")

# isspace: Verifica si el string contiene solo espacios en blanco (True/False)
print(f"isspace en texto6: {texto6.isspace()}")

# count: Cuenta el número de ocurrencias de una subcadena en el string
print(f"count en texto7: {texto7.count("Manzana")}")
