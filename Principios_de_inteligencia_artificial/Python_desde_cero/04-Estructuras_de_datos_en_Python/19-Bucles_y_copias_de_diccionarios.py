diccionario = {
    "Nombre": "Mike MV",
    "Edad": 25,
    "Ciudad": "México",
    "Profesión": "Estudiante",
    "Tecnologias": ["Python", "JavaScript", "HTML", "CSS"],
}

# CREACIÓN DE COPIAS
# PARA LA CREACIÓN DE COPIAS DE LAS ESTRUCTURAS DE DATOS SE DEBE USAR
# EL MÉTODO COPY DE LA ESTRUCTURA, YA QUE EN CASO DE HACER LO SIGUIENTE:
# diccionario2 = diccionario
# SE ESTARIA HACIENDO UNA REFERENCIA A LA ESTRUCTURA ORIGINAL, POR LO QUE
# AL HACER MODIFICACIONES EN ALGUNA DE LAS 2, AMBAS SE VERÁN AFECTADAS
diccionario2 = diccionario.copy()
print(diccionario2)

diccionario3 = dict(diccionario)
print(diccionario3)
print("------------------------------------------")

# BUCLE FOR
for key in diccionario:
    # Imprime las keys
    print(key)
    # Imprime los values
    print(diccionario[key])
print("------------------------------------------")

# IMPRESIÓN DE VALUES
for values in diccionario.values():
    print(values)
print("------------------------------------------")

# IMPRESIÓN DE KEYS
for key in diccionario.keys():
    print(key)
print("------------------------------------------")

# IMPRESIÓN DE KEY-VALUE
for key,value in diccionario.items():
    print(key)
    print(value)