import random

class Character:
    def __init__(self, name, health, attack, defense, level, exp):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = level
        self.exp = exp

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_dead(self):
        return self.health == 0

    def gain_exp(self, exp):
        self.exp += exp
        while self.exp >= self.level * 100:
            self.exp -= self.level * 100
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health += 10
        self.attack += 5
        self.defense += 5
        print(f"{self.name} has leveled up! Now at level {self.level}.")

    def special_ability(self):
        pass

class Mage(Character):
    def __init__(self):
        super().__init__("Mage", 70, 20, 5, 1, 0)

    def cast_spell(self, enemy):
        damage = self.attack * 2
        enemy.take_damage(damage)
        print(f"You cast a powerful spell dealing {damage} damage to the {enemy.name}!")

    def special_ability(self):
        return "1. Powerful spell"

class Knight(Character):
    def __init__(self):
        super().__init__("Knight", 100, 15, 10, 1, 0)

    def fortify(self):
        self.attack *= 1.5
        self.defense *= 1.5
        print("You have fortified your attack and defense for the next turn!")

    def special_ability(self):
        return "1. Fortify"

class Assassin(Character):
    def __init__(self):
        super().__init__("Assassin", 80, 25, 8, 1, 0)

    def critical_strike(self, enemy):
        crit_chance = 0.5
        if random.random() < crit_chance:
            damage = self.attack * 3
            print(f"Critical strike! You dealt {damage} damage to the {enemy.name}!")
        else:
            damage = self.attack
            print(f"You dealt {damage} damage to the {enemy.name}.")
        enemy.take_damage(damage)

    def special_ability(self):
        return "1. Critical strike"

class Tank(Character):
    def __init__(self):
        super().__init__("Tank", 120, 10, 15, 1, 0)

    def provoke(self, enemy):
        enemy.attack -= 5
        enemy.defense -= 5
        print(f"You have provoked the {enemy.name}, lowering its attack and defense!")

    def special_ability(self):
        return "1. Provoke"

class Enemy(Character):
    def __init__(self, name, health, attack, defense, level):
        super().__init__(name, health, attack, defense, level, 0)

def print_stats(character):
    print(f"{character.name}: Health {character.health}, Attack {character.attack}, Defense {character.defense}, Level {character.level}, EXP {character.exp}")

def choose_character():
    print("Choose your character:")
    print("1. Mage")
    print("2. Knight")
    print("3. Assassin")
    print("4. Tank")

    choice = int(input())
    if choice == 1:
        return Mage()
    elif choice == 2:
        return Knight()
        elif choice == 3:
        return Assassin()
    elif choice == 4:
        return Tank()
    else:
        print("Invalid choice, try again.")
        return choose_character()

def create_enemy(player_level):
    enemy_types = [
        ("Goblin", 50, 10, 5, 1),
        ("Orc", 80, 15, 10, 3),
        ("Troll", 100, 20, 15, 5)
    ]
    enemy = random.choice(enemy_types)
    level_diff = player_level - enemy[4]
    enemy = Enemy(*enemy)
    for _ in range(level_diff):
        enemy.level_up()
    return enemy

def special_ability_menu(player):
    print("Choose a special ability:")
    print(player.special_ability())

    choice = int(input())
    if choice == 1:
        return True
    else:
        print("Invalid choice, try again.")
        return special_ability_menu(player)

def battle_menu(player, enemy):
    print("Battle options:")
    print("1. Attack")
    print("2. Defend")
    print("3. Use special ability")
    print("4. Use potion")
    print("5. Flee")

    choice = int(input())

    if choice == 1:
        damage = max(0, player.attack - enemy.defense)
        enemy.take_damage(damage)
        print(f"You dealt {damage} damage to the {enemy.name}!")
    elif choice == 2:
        print("You brace yourself for the next attack.")
    elif choice == 3:
        if special_ability_menu(player):
            if isinstance(player, Mage):
                player.cast_spell(enemy)
            elif isinstance(player, Knight):
                player.fortify()
            elif isinstance(player, Assassin):
                player.critical_strike(enemy)
            elif isinstance(player, Tank):
                player.provoke(enemy)
    elif choice == 4:
        print("You drink a potion.")
        player.health += 30
        player.attack += 5
        player.defense += 5
    elif choice == 5:
        print("You attempt to flee...")
        if random.random() < 0.5:
            print("You escaped!")
            return True
        else:
            print("You failed to flee.")
    else:
        print("Invalid choice, try again.")
        return battle_menu(player, enemy)

    return False

def enemy_turn(player, enemy):
    damage = max(0, enemy.attack - player.defense)
    player.take_damage(damage)
    print(f"The {enemy.name} dealt {damage} damage to you!")

def main():
    print("Welcome to the RPG game!")

    player = choose_character()
    print(f"You have chosen the {player.name}.")
    print_stats(player)

    while True:
        enemy = create_enemy(player.level)
        print(f"A wild {enemy.name} has appeared!")
        print_stats(enemy)

        while not player.is_dead() and not enemy.is_dead():
            if battle_menu(player, enemy):
                break

            if enemy.is_dead():
                print(f"You have defeated the {enemy.name}!")
                player.gain_exp(enemy.level * 50)
            else:
                enemy_turn(player, enemy)

                if player.is_dead():
                    print(f"You have been defeated by the {enemy.name}.")
                    print("Game over.")
                    return

            print_stats(player)

        if player.is_dead():
            break

        print("Do you want to continue? (yes/no)")
        continue_game = input().lower()
        if continue_game == "no":
            print("Thank you for playing!")
            break

        if __name__ == "__main__":
            main()

