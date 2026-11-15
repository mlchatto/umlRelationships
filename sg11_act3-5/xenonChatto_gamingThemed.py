class Hero():
    def __init__(self, name: str, health: int, move: str, speed: int):
        self.name = name
        self.health = health
        self.move = move
        self.speed = speed

class Potions():
    def __init__(self, name: str, effect: str):
        self.name = name
        self.effect = effect

class Mage(Hero):
    def __init__(self, name: str, move: str):
        super().__init__(name, 100, move, 10)
        self.name = "Mage"

    def move(self):
        print(f"{self.name} casts a powerful spell!")

class Warrior(Hero):
    def __init__(self, name: str, move: str):
        super().__init__(name, 100, move, 5)
        self.name = "Warrior"

    def move(self):
        print(f"{self.name} swings a mighty sword!")

class Archer(Hero):
    def __init__(self, name: str, move: str):
        super().__init__(name, 100, move, 8)
        self.name = "Archer"

    def move(self):
        print(f"{self.name} shoot a precise arrow!")

class HealthPotion(Potions):
    def __init__(self):
        super().__init__("Health Potion", "You regain 50 HP!")

class ManaPotion(Potions):
    def __init__(self):
        super().__init__("Mana Potion", "You restore 30 MP!")

class SpeedBoost(Potions):
    def __init__(self):
        super().__init__("Speed Boost", "Your speed increases for 10 seconds!")


heroes = [Mage("Mage", "Chain Lightning"), Warrior("Knight", "Dual Wield"), Archer("Elf", "Focus Fire")]
potions = [HealthPotion(), ManaPotion(), SpeedBoost()]

for hero in heroes:
    print(f"{hero.name} uses {hero.move}.")