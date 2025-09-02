import random


x = 1  # int
y = 2.8  # float
z = 1j  # complex

print(type(x))
print(type(y))
print(type(z))

# Casteo de tipos
a = float(x) # int a float
b = int(y) # float a int
c = complex(x) # int a complex

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Números alaatorios
random_number = random.randrange(1, 10) # Número aleatorio entre 1 y 10, excluyendo el 10
print(random_number)

random_number2 = random.randint(1, 10) # Número aleatorio entre 1 y 10, incluyendo el 10
print(random_number2)

# Número entre 0 y 1
random_float = random.random() # Número aleatorio entre 0 y 1
print(random_float)