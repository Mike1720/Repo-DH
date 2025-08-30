# Juego de adivinanza
import random

minor = 1
major = 11
secret_number = random.randint(minor,major)  # Número secreto entre 1 y 100
is_guessed = False
attepmts = 0
max_attempts = 3

print("¡Bienvenido al juego de adivinanza!")
print(f"Tienes {max_attempts} intentos para adivinar el número secreto entre {minor} y {major - 1}")

while not is_guessed:
    user_number = int(input("¿Cuál es tu número?: "))
    if user_number < 1 or user_number > 10:
        print("Número fuera de rango. Ingresa un número entre 1 y 10.")
    else:
        if user_number != secret_number:
            attepmts += 1
            if attepmts >= max_attempts:
                print(f"Has agotado tus intentos. El número secreto era {secret_number}.")
                break
            if user_number < secret_number:
                print(f"El número secreto es mayor. Intenta de nuevo, te quedan {max_attempts - attepmts} intentos.")
            else:
                print(f"El número secreto es menor. Intenta de nuevo, te quedan {max_attempts - attepmts} intentos.")
        else:
            is_guessed = True
            print(f"¡Felicidades! Has adivinado el número secreto en {attepmts + 1} intentos.")




