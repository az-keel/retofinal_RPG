import personajes

def main():
    print("¡Bienvenido al juego de rol!")
    player_name = input("Por favor, ingrese su nombre de jugador: ")
    player_class = select_class()

    player = player_class(player_name)

    print(f"\n¡Bienvenido, {player.name}!")
    print(f"Tú eres un {player.__class__.__name__} de nivel {player.level}.\n{player.stats}")

    enemies = generate_enemies(3)
    print(f"\nTe has encontrado con {len(enemies)} enemigos.")
    for i, enemy in enumerate(enemies):
        print(f"Enemigo {i+1}: {enemy.name} ({enemy.stats})")

    input("\nPresiona ENTER para comenzar la batalla.")

    while player.is_alive() and len(enemies) > 0:
        enemy = select_enemy(enemies)

        print(f"\n¡Es el turno de {player.name}!")
        player.attack(enemy)

        if not enemy.is_alive():
            print(f"\n¡Has derrotado a {enemy.name}!")
            enemies.remove(enemy)
            if len(enemies) == 0:
                break

        for enemy in enemies:
            if enemy.is_alive():
                print(f"\n¡Es el turno de {enemy.name}!")
                enemy.attack(player)

                if not player.is_alive():
                    print("\n¡Has sido derrotado! Game Over.")
                    return

    print("\n¡Felicidades! Has ganado la batalla.")

def select_class():
    classes = {
        1: personajes.Mage,
        2: personajes.Knight,
        3: personajes.Assassin,
        4: personajes.Tank
    }

    while True:
        print("\nSelecciona una clase:")
        for key, value in classes.items():
            print(f"{key}. {value.__name__}")
        choice = input("Opción: ")
        if choice.isnumeric() and int(choice) in classes.keys():
            return classes[int(choice)]
        print("Por favor, ingrese una opción válida.")

def generate_enemies(num_enemies):
    enemies = [personajes.Goblin() for _ in range(num_enemies)]
    enemies.append(personajes.Orc())
    return enemies

def select_enemy(enemies):
    print("\nSelecciona un enemigo:")
    for i, enemy in enumerate(enemies):
        print(f"{i+1}. {enemy.name} ({enemy.stats})")
    choice = input("Opción: ")
    while not choice.isnumeric() or int(choice) < 1 or int(choice) > len(enemies):
        print("Por favor, ingrese una opción válida.")
        choice = input("Opción: ")
    return enemies[int(choice)-1]
