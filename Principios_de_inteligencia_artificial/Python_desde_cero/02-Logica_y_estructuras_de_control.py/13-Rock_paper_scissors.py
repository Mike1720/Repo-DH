# Juego de piedra, papel o tijeras
def rock_paper_scissors_1():
    """
    Juego de piedra, papel o tijeras
    """
    player1_name = input("Nombre del jugador 1: ")
    player2_name = input("Nombre del jugador 2: ")

    player1 = input(f"{player1_name}, elige piedra, papel o tijeras: ").lower()
    player2 = input(f"{player2_name}, elige piedra, papel o tijeras: ").lower()

    if player1 == player2:
        print("Empate!")
    elif (
        (player1 == "piedra" and player2 == "tijeras")
        or (player1 == "papel" and player2 == "piedra")
        or (player1 == "tijeras" and player2 == "papel")
    ):
        print(f"Ha ganado {player1_name}!")
    else:
        print(f"Ha ganado el {player2_name}!")

# rock_paper_scissors_1()


def rock_paper_scissors_2():
    player1_name = input("Nombre del jugador 1: ")
    player2_name = input("Nombre del jugador 2: ")
    isFinished = False
    choices = ["piedra", "papel", "tijeras"]

    while not isFinished:
        player1_choice = input(
            f"{player1_name}, elige piedra, papel o tijeras: "
        ).lower()

        player2_choice = input(
            f"{player2_name}, elige piedra, papel o tijeras: "
        ).lower()
            
        
        if player1_choice not in choices or player2_choice not in choices:
            print("Elección inválida. Inténtalo de nuevo.")
            continue

        if player1_choice == player2_choice:
            print("Empate!")
        elif (
            (player1_choice == "piedra" and player2_choice == "tijeras")
            or (player1_choice == "papel" and player2_choice == "piedra")
            or (player1_choice == "tijeras" and player2_choice == "papel")
        ):
            print(f"Ha ganado {player1_name}!")
            isFinished = True
        else:
            print(f"Ha ganado {player2_name}!")
            isFinished = True
    print("Bien jugado!")

rock_paper_scissors_2()
