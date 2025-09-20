import random
from Class.Player import Player
from Class.Enemy import Enemy


def main():
    player_name = input(
        "Bienvenido a la aventura en el espacio! Por favor ingresa tu nombre: "
    )

    player = Player(player_name)
    enemies = [Enemy("Alien", 50, 10), Enemy("Robot", 30, 5), Enemy("Monstruo", 70, 15)]
    defeated_enemies = []

    print("Comienza la aventura")

    while enemies:
        current_enemy = random.choice(enemies)
        if current_enemy in defeated_enemies:
            continue

        print(f"Te encuentras con un {current_enemy.name} enemigo")
        while current_enemy.health > 0:
            action = input("¿Que deseas hacer? (atacar/huir)").lower()
            if action == "atacar":
                damage_player = player.attack()
                print(
                    f"Has atacado al {current_enemy.name} y le has causado {damage_player} de daño"
                )
                current_enemy.take_damage(damage_player)

                if current_enemy.health > 0:
                    damage_enemy = current_enemy.attack()
                    print(
                        f"El {current_enemy.name} te atacó y te causó {damage_enemy} de daño"
                    )
                    player.take_damage(damage_enemy)
            elif action == "huir":
                print("Has decidido huír del combate")
                print("COBARDE!")
                break
        if player.health <= 0:
            print("¡Has perdido la partida!")
            break
        player.gain_experience(20)
        if current_enemy.health <= 0:
            defeated_enemies.append(current_enemy)
            enemies.remove(current_enemy)

        keep_going = input("¿Quieres seguir explorando? (s/n): ").lower()

        if keep_going != "s":
            print("Gracias por haber jugado")
            break
    if not enemies:
        print("Felicidades! Has derrotado a todos los enemigos")


if __name__ == "__main__":
    main()
