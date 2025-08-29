# Estructura de control while
# La estructura de control while se utiliza para repetir un bloque de código mientras una condición sea verdadera.

contador = 0
while contador < 5:
    print(f"El contador es: {contador}")
    contador += 1
print(f"Fin del bucle while. Valor final del contador:{contador}")
# En este ejemplo, el bucle while se ejecuta MIENTRAS la variable contador sea menor que 5, por lo que solo se imprimen los valores del 0 al 4, teniendo como valor final de contador el 5.


counter = 0
limit = 5
sumatoria = 0

while counter < limit:
    sumatoria += counter
    counter += 1
print(f"La sumatoria de los números del 0 al {limit-1} es: {sumatoria}")
