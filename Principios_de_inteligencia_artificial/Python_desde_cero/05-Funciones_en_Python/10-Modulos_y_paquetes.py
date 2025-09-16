# ARCHIVO PRINCIPAL

# IMPORTACION COMPLETA DEL ARCHIVO
from Calculos_Modulos_Paquetes import Operaciones

# IMPORTACION DE FUNCIONES SELECTAS
from Calculos_Modulos_Paquetes.Aux_Modulos import es_par, es_primo

resultado_suma = Operaciones.suma(10, 5)
resultado_resta = Operaciones.resta(10, 5)
resultado_division = Operaciones.division(10, 5)
resultado_multiplicacion = Operaciones.multiplicacion(10, 5)
is_odd = es_par(10)
is_prime = es_primo(10)

print(resultado_suma)
print(resultado_resta)
print(resultado_division)
print(resultado_multiplicacion)
print(is_odd)
print(is_prime)
