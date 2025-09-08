# FUNCIONES
# Sintaxis

# def nombre_de_la_funcion(parametros):
#   """Docstring de la función"""
#   Cuerpo de la función
#   return resultado


def saludar1(nombre):
    """ "
    Función que recibe como parametro OBLIGATORIO el nombre
    del usuario.
    Imprime por consola el mensaje: "Hola nombre_usuario"
    NO DEVUELVE NINGÚN RESULTADO
    """
    print(f"Hola {nombre}!")


#       Argumento que se le pasa a la función
saludar1("Miguel")


def saludar2():
    """
    Función que no recibe ningún parametro.
    Imprime por consola el mensaje: "Hola!"
    """
    print("Hola!")


saludar2()


def saludar3(nombre=""):
    """
    Función que puede recibir como parametro un argumento,
    En caso de recibirlo imprimirá por consola el mensaje:
    "Hola! nombre, mucho gusto"
    Caso contrario imprimirá el mensaje:
    "Hola!!!"
    """
    if nombre != "":
        print(f"Hola! {nombre}, mucho gusto")
    else:
        print("Hola!!!")


saludar3()
saludar3("Mike")


#               tupla, valor_predefinido
def sumatoria(*numeros, x=20):
    """Función que recibe como parametros una cantidad indeterminada
    de números. Estó se logra mediante la adición del asterico (*) al
    inicio del parametro

    Returns:
        number: Sumatoria de los números ingresado
    """
    suma = 0
    # x = 10 -> Sobreescribe el valor predefinido (20)
    for numero in numeros:
        suma += numero
    return suma + x

#                     |     tupla   |
sumatoria = sumatoria(10, 20, 30, 10, x=4)
print(sumatoria)

# NOTA GENERAL:
# LOS PARAMETROS PREDETERMINADOS DEBEN SER ESCRITOS AL FINAL
# DE TODOS LOS PARAMETROS, YA QUE EN CASO CONTRARIO GENERARÁ ERROR


def papa_orgulloso(kid1, kid3, kid2):
    print(f"Mis hijos son: {kid1}, {kid2} y {kid3}")
    print(f"Y la más pequeña es {kid3}")


# Aurora es la más pequeña

papa_orgulloso("Alan", "Amairani", "Aurora")
# Expected: Mis hijos son Alan, Amairani y Aurora
# Output: Mis hijos son Alan, Aurora y Amairani

# Para dar el orden correcto a la identidad de los argumentos, se hace
# uso de las keyword arguments, las cuales indican el valor para
# cada argumento.
papa_orgulloso(kid1="Alan", kid2="Amairani", kid3="Aurora")


def papa_orgulloso2(**kids):
    print(f"Mis hijos son: {kids["a"]}, {kids["b"]} y {kids["c"]}")
    print(f"Y la más pequeña es {kids["c"]}")


papa_orgulloso2(a="Alan", b="Amairani", c="Aurora")
