# Definir el valor actual del Euro y Dólar con respecto al Peso Mexicano
EUR_MXN = 23.70
USD_MXN = 20.75

# Solicitar al usuario el tipo de conversión de (EUR-MXN o USD-MXN)
tipo_cambio = input("Ingrese la moneda origen para la conversión (EUR/USD): ").upper()

# Solicitar el monto a convertir
monto = float(input("Ingrese el monto a convertir: "))

# Realizar la conversión utilizando el tipo de cambio correspondiente
resultado = 0
if tipo_cambio == "EUR":
    resultado = EUR_MXN * monto
elif tipo_cambio == "USD":
    resultado = USD_MXN * monto
else:
    print("Tipo de cambio no válido")

if resultado != 0:
    print(f"El resultado de la conversión es: {resultado}")
