from personajes import *
from pociones import* 
from LogicaJuego import*
import random

def main():
    print("¡Bienvenido al juego de rol!")
    player_name = input("Por favor, ingresa tu nombre: ")
    player_class = choose_player_class()
    player = player_class(player_name)
    print(f"¡{player_name}, eres un {player_class.__name__}!")
    print(f"Tus estadísticas son: {player.stats}")
    enemy = Goblin()
    print(f"¡Un {enemy.name} salvaje aparece!")
    while player.is_alive() and enemy.is_alive():
        print(f"\n{player_name}: {player.hp} HP | {enemy.name}: {enemy.hp} HP")
        player.attack(enemy)
        if enemy.is_alive():
            enemy.attack(player)
        else:
            print(f"\n¡Has derrotado al {enemy.name}!")
            break
        input("\nPresiona Enter para continuar...")
    if player.is_alive():
        print("\n¡Has ganado el combate!")
    else:
        print("\n¡Has perdido el combate!")
        
def choose_player_class():
    print("\nPor favor, elige una clase:")
    print("1. Mago")
    print("2. Caballero")
    print("3. Asesino")
    print("4. Tanque")
    choice = input("Ingresa el número de la clase que quieres jugar: ")
    if choice == "1":
        return Mage
    elif choice == "2":
        return Knight
    elif choice == "3":
        return Assassin
    elif choice == "4":
        return Tank
    else:
        print("¡Esa no es una opción válida!")
        return choose_player_class()

if __name__ == "__main__":
    main()
