diccionario = {
    "Nombre": "Mike MV",
    "Edad": 25,
    "Ciudad": "México",
    "Profesión": "Estudiante",
    "Tecnologias": ["Python", "JavaScript", "HTML", "CSS"],
}

print(diccionario)
print("------------------------------------------")

# MODIFICACIÓN Y AGREGADO DE PARES KEY-VAUE
diccionario.update({"Nombre": "Miguel Miranda", "Edad": 24})
diccionario.update({"Comida Fav": ["Pizza", "Tacos", "Pozole"]})
print(diccionario)
print("------------------------------------------")


# ELIMINACIÓN DE PARES
diccionario.pop("Ciudad")
print(diccionario)
print("------------------------------------------")

diccionario.popitem()
print(diccionario)
print("------------------------------------------")

