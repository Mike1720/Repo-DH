from Class.Mago import Mago

merlin = Mago("Merlin", ["Bola de fuego", "Rayo"])
copia_merlin = Mago("Merlin", ["Bola de fuego", "Rayo"])
gandalf = Mago("Gandalf", ["Llamar a las aguilas", "Bola de fuego"])

print(merlin)  # Devuelve el método __str__
print(len(merlin))  # Devuelve el método __len__

print(gandalf)  # Devuelve el método __str__
print(len(gandalf))  # Devuelve el método __len__

print(merlin == gandalf)
# Devuelve una comparación de los datos almacenados, no del lugar de memoria
print(merlin == copia_merlin)

mago_combinado = merlin + gandalf
print(mago_combinado)
