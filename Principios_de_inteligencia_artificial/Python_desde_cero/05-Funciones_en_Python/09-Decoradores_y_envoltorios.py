# DECORADOR

# Un decorador es simplemente una función que recibe otra función como argumento y regresa una nueva función.
# Se usan para añadirle funcionalidades extras a una función sin tener que modificar su código original.

# ENVOLTORIOS (WRAPPERS)

# El envoltorio (o wrapper) es la función interna que se encarga de "envolver" a la función original para darle ese extra.

def decorador(func):
    def envoltorio():
        print(
            "Esta funcionalidad se dispararía antes de la función que nos pasen como parametro"
        )
        func()
        print(
            "Esta funcionalidad se dispararía después de la función que nos pasen como parametro"
        )

    return envoltorio


def saludar():
    print("Hola!")


saludo_personalizado = decorador(saludar)
saludo_personalizado()
