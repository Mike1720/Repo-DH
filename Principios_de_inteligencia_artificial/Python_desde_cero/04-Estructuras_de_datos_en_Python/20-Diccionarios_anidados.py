famila = {
    "Padre": {"Nombre": "Pedro Ramirez", "Profesión": "Chofer"},
    "Madre": {"Nombre": "Patricia Martinez", "Profesión": "Abogada"},
    "Hijo": {"Nombre": "Miguel Miranda", "Profesión": "Estudiante"},
}
print(famila)
print(famila["Padre"]["Nombre"])
print("------------------------------------------")


padre = {"Nombre": "Pedro Ramirez", "Profesión": "Chofer"}
madre = {"Nombre": "Patricia Martinez", "Profesión": "Abogada"}
hijo = {"Nombre": "Miguel Miranda", "Profesión": "Estudiante"}
famila2 = {"Padre": padre, "Madre": madre, "Hijo": hijo}
print(famila2)
print("------------------------------------------")

for pariente, data in famila2.items():
    print(pariente)
    for clave in data:
        print(f"{clave}: {data[clave]}")
