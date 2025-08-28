# Operadores de comparación
# Los operadores de comparación se utilizan para comparar dos valores y devuelven un valor booleano (True o False) según el resultado de la comparación.

# Variables de ejemplo
a = 5
b = 5
c = 3

print(
    """Valores de las variables:
      a = {}
      b = {}
      c = {}
""".format(
        a, b, c
    )
)

# Igualdad (==)
print("a == b: {}".format(a == b))
print("a == c: {}".format(a == c))

# Desigualdad (!=)
print("a != b: {}".format(a != b))
print("a != c: {}".format(a != c))

# Mayor que (>)
print("a > c: {}".format(a > c))
print("c > a: {}".format(c > a))
print("b > a: {}".format(b > a))

# Menor que (<)
print("c < a: {}".format(c < a))
print("a < c: {}".format(a < c))
print("b < a: {}".format(b < a))

# Mayor o igual que (>=)
print("a >= c: {}".format(a >= c))
print("c >= a: {}".format(c >= a))
print("b >= a: {}".format(b >= a))

# Menor o igual que (<=)
print("a <= c: {}".format(a <= c))
print("c <= a: {}".format(c <= a))
print("b <= a: {}".format(b <= a))

