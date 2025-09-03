# Paso 1: Solicitar al usuario que ingrese la edad del cliente.
#Mostrar mensaje: "Por favor, ingrese la edad del cliente"
#Leer el dato ingresado y asignarlo a la variable edad
edad = int(input("Por favor, ingrese la edad del cliente: "))

# Paso 2: Verificar si la edad ingresada cumple con el requisito para ingresar a la discoteca.
#Si edad >= 18
#    asignarle a la variable es_permitido que sea verdadero.
#Sino
#    asignarle a la variable es_permitido que sea falso.
#Fin Si
es_permitido = True if edad >= 18 else False

# Paso 3: Mostrar al usuario si su cliente puede o no ingresar a la discoteca.
#Si es_permitido es verdadero
#    Mostrar mensaje: "¡Puedes ingresar a la discoteca!"
#Sino
#    Mostrar mensaje: "Lo sentimos mucho, no puedes ingresar a la discoteca siendo menor de edad"
#Fin Si

if es_permitido:
    print("¡Puedes ingresar a la discoteca!")
else:
    print("Lo sentimos mucho, no puedes ingresar a la discoteca siendo menor de edad")
