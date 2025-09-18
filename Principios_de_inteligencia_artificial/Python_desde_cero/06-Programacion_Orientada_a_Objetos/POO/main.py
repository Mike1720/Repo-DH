from Class.Perro import Perro

# ---------------------------------------------


# 2.- CREACIÓN DE INSTANCIAS
perro1 = Perro("Fenrir", 3)
perro2 = Perro("Zaki", 10)


# ---------------------------------------------


# 3.- ACCESO A MÉTODOS Y ATRIBUTOS DE LA CLASE
sonido_perro1 = perro1.ladrar()  # ¡Guau!
nombre_perro1 = perro1.nombre  # Fenrir
edad_perro1 = perro1.edad  # 3

print(
    f"El perro1 se llama {nombre_perro1}, tiene {edad_perro1} años y hace {sonido_perro1}"
)

print(
    f"El perro2 se llama {perro2.nombre}, tiene {perro2.edad} años y hace {perro2.ladrar()}"
)
