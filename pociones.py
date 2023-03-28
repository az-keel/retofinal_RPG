import random

class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.potions = {"attack": 0, "defense": 0}

    def __str__(self):
        return f"{self.name} ({self.player_class}) - Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}"

    def use_potion(self, potion_type):
        if self.potions[potion_type] > 0:
            if potion_type == "attack":
                self.attack += 5
                self.potions[potion_type] -= 1
                print(f"{self.name} used an attack potion. Attack increased by 5.")
            elif potion_type == "defense":
                self.defense += 5
                self.potions[potion_type] -= 1
                print(f"{self.name} used a defense potion. Defense increased by 5.")
        else:
            print("You don't have any of that type of potion.")

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage < 0:
            damage = 0
        enemy.health -= damage
        if enemy.health < 0:
            enemy.health = 0
        print(f"{self.name} attacks {enemy.enemy_type} with a damage of {damage}.")
        print(f"{enemy.enemy_type} health: {enemy.health}")

class Enemy:
    def __init__(self, enemy_type, health, attack, defense):
        self.enemy_type = enemy_type
        self.health = health
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.enemy_type} - Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}"

    def attack_player(self, player):
        damage = self.attack - player.defense
        if damage < 0:
            damage = 0
        player.health -= damage
        if player.health < 0:
            player.health = 0
        print(f"{self.enemy_type} attacks {player.name} with a damage of {damage}.")
        print(f"{player.name} health: {player.health}")

def main():
    player_name = input("Enter your name: ")
    player_class = input("Enter your class (mage, knight, assassin, tank): ")

    player = Player(player_name, player_class)

    print(f"Welcome, {player.name} the {player.player_class}!")
    print(player)

    enemies = []
    num_enemies = 3
    for i in range(num_enemies):
        enemy_type = random.choice(["Goblin", "Orc"])
        health = random.randint(70, 100)
        attack = random.randint(10, 15)
        defense = random.randint(5, 10)
        enemy = Enemy(enemy_type, health, attack, defense)
        enemies.append(enemy)

    print("You will be fighting the following enemies:")
    for i, enemy in enumerate(enemies):
        print(f"{i+1}. {enemy}")

    for enemy in enemies:
        while enemy.health > 0:
            print()
            print(f"Select an enemy to attack:")
            for i, e in enumerate(enemies):
                player.use_potion(potion_type)



        print(f"{i+1}. {e.enemy_type} - Health: {e.health}")

        enemy_choice = int(input("Enter enemy number: ")) - 1

        if enemy_choice < 0 or enemy_choice >= len(enemies):
            print("Invalid choice.")
            continue

        enemy_to_attack = enemies[enemy_choice]
        player_choice = input("Do you want to attack or use a potion? (attack/potion): ")

        if player_choice == "attack":
            player.attack_enemy(enemy_to_attack)
        elif player_choice == "potion":
            potion_type = input("Which potion do you want to use? (attack/defense): ")
            player.use_potion(potion_type)
        else:
            print("Invalid choice.")
            continue

        if enemy_to_attack.health == 0:
            print(f"{enemy_to_attack.enemy_type} has been defeated!")

            # Drop a potion
            potion_drop = random.choice(["attack", "defense"])
            player.potions[potion_drop] += 1
            print(f"{enemy_to_attack.enemy_type} dropped a {potion_drop} potion!")

            enemies.remove(enemy_to_attack)

            if len(enemies) == 0:
                print("Congratulations, you have defeated all the enemies!")
                return

        for enemy in enemies:
            if enemy.health > 0:
                enemy.attack_player(player)

        if player.health == 0:
            print("Game over. You have been defeated.")
            return

