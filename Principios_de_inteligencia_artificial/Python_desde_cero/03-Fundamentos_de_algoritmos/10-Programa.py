
# Solicitar al usuario las medidas de la pieza del mueble en cms
medida = float(input("Por favor, ingrese las medidas de la pieza del mueble en cm: "))

# Convertir las medidas de cms a pulgadas
conversion = round((medida / 2.54), 2)

# Mostrar las medidas convertidas en pulgadas al usuario
print(f"La medida de la pieza ingresada es {conversion} pulgadas")