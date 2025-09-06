conjunto_letras = {"a", "b", "c"}
conjunto_numeros = {1, 2, 3}
tupla_numeros = {1, 2, 3}

conjunto_union = conjunto_letras.union(conjunto_numeros)
# Abreviación
# conjunto_union = conjunto_letras | conjunto_numeros

conjunto_letras.update(tupla_numeros)

print(conjunto_union)
print(conjunto_letras)

set_chicago = {"Python", "JavaScript", "AWS"}
set_oxford = {"Python", "TypeScript", "GoogleCloud"}
# Intersection -> Elementos en común de ambos conjuntos
set3 = set_chicago.intersection(set_oxford)
# Abreviación
# set3 = set_tecnologias_uni_chicago & set_tecnologias_uni_oxford

# difference -> Elementos unicos del primer conjunto
set4 = set_chicago.difference(set_oxford)
# Abreviación
# set4 = set_chicago - set_oxford

print(set3)
print(set4)

# LA UNICA MANERA DE RECORRER UN SET ES MEDIANTE BUCLE FOR
conjunto_frutas = {"Manzana", "Naranja", "Banana"}
for fruta in conjunto_frutas:
    print(fruta)
