# ---------------------------------------------


# 1.- CREACIÓN DE CLASE
class Perro:
    # Método constructor (__init__)
    def __init__(self, nombre, edad):
        # --------ATRIBUTOS--------
        # Al atributo "nombre" le asignamos "nombre" que nos envian como argumento en el constructor
        self.nombre = nombre
        # Al atributo "edad" le asignamos "edad" que nos envian como argumento en el constructor
        self.edad = edad

    # --------MÉTODOS--------
    def ladrar(self):
        return "¡Guau!"

