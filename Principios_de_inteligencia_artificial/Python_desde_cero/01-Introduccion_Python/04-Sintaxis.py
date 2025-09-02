#SINTAXIS DE PYTHON
"""
    Son reglas que se deben seguir al escribir el código para que sea valido y 
    pueda ser interpretado correctamente.
"""

# Indentación
"""
    La indentación es el espacio en blanco al inicio de una línea de código.
    Es el equivalente a las llaves en otros lenguajes de programación, cuya 
    función es agrupar en bloques de código.
"""

# Manera correcta de usar la indentación
for i in range (5):
    print(i) # Imprime los números del 0 al 4
print(i) # Imprime el último valor de i, que es 4, ya que no se encuentra dentro del mismo "bloque" de código que el bucle for.


# Manera incorrecta de usar la indentación
#for j in range(5):
#print(j) # Genera un error de sintaxis porque no se ha indentado correctamente.