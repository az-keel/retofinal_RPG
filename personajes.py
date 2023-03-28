class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_hp = 10
        self.hp = self.max_hp
        self.attack = 1
        self.defense = 1
        self.speed = 1

    @property
    def stats(self):
        return f"Nivel: {self.level} | HP: {self.max_hp} | Ataque: {self.attack} | Defensa: {self.defense} | Velocidad: {self.speed}"

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage > 0:
            enemy.hp -= damage
            print(f"\n¡{self.name} ha causado {damage} puntos de daño!")
        else:
            print(f"\n¡{self.name} no ha logrado causar daño!")
            
    def attack(self, target):
        self.attack_enemy(target)

    def is_alive(self):
        return self.hp > 0

class Mage(Player):
    def __init__(self, name):
        super().__init__(name)
        self.max_hp = 8
        self.hp = self.max_hp
        self.attack = 3
        self.defense = 1
        self.speed = 2

class Knight(Player):
    def __init__(self, name):
        super().__init__(name)
        self.max_hp = 12
        self.hp = self.max_hp
        self.attack = 2
        self.defense = 3
        self.speed = 1

class Assassin(Player):
    def __init__(self, name):
        super().__init__(name)
        self.max_hp = 6
        self.hp = self.max_hp
        self.attack = 4
        self.defense = 0
        self.speed = 3

class Tank(Player):
    def __init__(self, name):
        super().__init__(name)
        self.max_hp = 15
        self.hp = self.max_hp
        self.attack = 1
        self.defense = 4
        self.speed = 1

class Enemy:
    def __init__(self, name, max_hp, attack, defense, speed):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

    @property
    def stats(self):
        return f"HP: {self.max_hp} | Ataque: {self.attack} | Defensa: {self.defense} | Velocidad: {self.speed}"

    def attack_player(self, player):
        damage = self.attack - player.defense
        if damage > 0:
            player.hp -= damage
            print(f"\n¡{self.name} ha causado {damage} puntos de daño!")
        else:
            print(f"\n¡{self.name} no ha logrado causar daño!")

    def attack(self, target):
        self.attack_player(target)

    def is_alive(self):
        return self.hp > 0

class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 5, 1, 0, 1)

class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", 8, 2, 1, 1)

class Dragon(Enemy):
    def __init__(self):
        super().__init__("Dragon", 15, 4, 2, 1)
