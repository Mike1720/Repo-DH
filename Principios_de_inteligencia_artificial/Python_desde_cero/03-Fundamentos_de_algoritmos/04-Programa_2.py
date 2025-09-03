# Paso 1: Solicitar al usuario que ingrese el radio del círculo.
# Mostrar mensaje: "Por favor, ingrese el radio del círculo"
# Leer dato ingresado y asignarlo a variable radio
import math

radio = float(input("Por favor, ingrese el radio del círculo: "))

## Paso 2: Calcular el área del circulo utilizando la formula area = π * radio^2.
## Definir y asignar a la variable area el resultado de π por radio al cuadrado.
area = math.pi * (radio ** 2)

## Paso 3: Monstrar al usuario el área calculada.
## Mostrar mensaje: "El área del circulo con radio", radio, "es", area
print(f"El área del círculo con radio {radio} es {area}")