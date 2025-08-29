# Estructura de control if, elif, else
# Permite ejecutar diferentes bloques de código según ciertas condiciones

x = 10

if x > 5:
    print("x es mayor a 5")
elif x > 0:
    print("x es mayor a 0")
else:
    print("x es menor a cero")


# Suponiendo un caso de viaje

visa = False
passport = False

# if visa and passport:
#     print("Puedes viajar a cualquier país")
# elif passport and not visa:
#     print("Puedes viajar a paises que no requieren visa")
# else:
#     print("Debes de obtener la documentación necesaria para viajar")

if visa and passport:
    print("Puedes viajar a cualquier lugar")
elif passport or visa:
    print("Puedes viajar a algunos lugares")
else:
    print("No puedes viajar a nungun lugar")


# Otro ejemplo

edad = 17
if edad < 18 or edad > 60:
    if edad < 18:
        print("No tienes edad suficiente para entrar al concierto")
    else:
        print("Por cuestión de seguridad no se permite el ingreso a mayores de 60 años")
else:
    print("Puedes entrar al concierto")
