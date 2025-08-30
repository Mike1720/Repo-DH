# Palabras clave de estructuras de control en Python

# break: Termina un bucle antes de que haya iterado sobre todos los elementos.
counter = 0
while counter < 10:
    print(counter)
    if counter == 5:
        print("Se alcanzó el valor de 5, saliendo del bucle.")
        break
    counter += 1
print(counter) # Al haber alcanzado el break, lo que se encuentra después ya no es ejecutado. De esta manera, el valor de counter es 5, no 6.

# continue: Salta a la siguiente iteración del bucle, omitiendo el resto del código en la iteración actual.
for i in range(10):
    if i % 2 == 0:
        continue  # Salta los números pares
    print(i)  # Solo imprime números impares

count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)

# pass: Es un marcador de posición que no hace nada. Se utiliza cuando se requiere una declaración sintácticamente, pero no se necesita ninguna acción.
edad = 18
if edad > 18:
    print("Puedes ingresar a la fiesta.")
elif edad == 18:
    pass
else:
    print("No puedes ingresar a la fiesta.")
    