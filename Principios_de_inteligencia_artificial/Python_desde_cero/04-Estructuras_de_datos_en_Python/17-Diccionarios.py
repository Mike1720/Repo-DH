# ------------------------------
# DICCIONARIOS
# ------------------------------

diccionario = {
    "Nombre": "Mike MV",
    "Edad": 25,
    "Ciudad": "México",
    "Profesión": "Estudiante",
    "Tecnologias": ["Python", "JavaScript", "HTML", "CSS"],
}

# VISUALIZACIÓN DE ELEMENTOS
print(diccionario)
print(diccionario["Nombre"])
print(diccionario["Tecnologias"][1])
print("------------------------------------------")


# ASGINACIÓN DE VALOR A VARIABLE
nombre = diccionario.get("Nombre")
print(nombre)
print("------------------------------------------")


# MODIFICACIÓN DE VALORES
diccionario["Nombre"] = "Miguel Miranda"
print(diccionario)
print("------------------------------------------")


# AGREGADO DE PAR KEY-VALUE
diccionario["Comida Favorita"] = ["Pizza", "Pozole", "Tacos"]
print(diccionario)
print("------------------------------------------")


# VISUALIZACIÓN DE KEYS
keys = diccionario.keys()
print(keys)
print("------------------------------------------")


# VISUALIZACIÓN DE VALUES
values = diccionario.values()
print(values)
print("------------------------------------------")

# 
items = diccionario.items()
print(items)
print("------------------------------------------")

if "Nombre" in diccionario:
    print("Existe la clave")