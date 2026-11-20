class Hero():
    def __init__(self, name: str, health: int, move: str, speed: int, mana: int):
        self.name = name
        self.health = health
        self.move = move
        self.speed = speed
        self.mana = mana

class Potions():
    def __init__(self, name: str, effect: str):
        self.name = name
        self.effect = effect

class Mage(Hero):
    def __init__(self, name: str, move: str):
        super().__init__(name, 100, move, 10, 100)
        self.name = "Wizard"

    def move(self):
        print(f"{self.name} casts a powerful spell!")

class Warrior(Hero):
    def __init__(self, name: str, move: str):
        super().__init__(name, 100, move, 5, 100)
        self.name = "Knight"

    def move(self):
        print(f"{self.name} swings a mighty sword!")

class Archer(Hero):
    def __init__(self, name: str, move: str):
        super().__init__(name, 100, move, 8, 100)
        self.name = "Elf"

    def move(self):
        print(f"{self.name} shoot a precise arrow!")

class HealthPotion(Potions):
    def __init__(self, name: str, effect: str):
        super().__init__(name, effect)
        self.name = "Health Potion"

    def use(self, hero: Hero):
        if hero.health == hero.health:
            hero.health = hero.health
        else:
            hero.health += 50
        print(f"{hero.name} uses {self.name}. {self.effect} Now has {hero.health} HP.")

class ManaPotion(Potions):
    def __init__(self, name: str, effect: str):
        super().__init__(name, effect)
        self.name = "Mana Potion"

    def use(self, hero: Hero):
        if hero.health == hero.health:
            hero.health = hero.health
        else:
            hero.health += 50
        print(f"{hero.name} uses {self.name}. {self.effect} Now has {hero.health} HP.")

class SpeedBoost(Potions):
    def __init__(self, name: str, effect: str):
        super().__init__(name, effect)
        self.name = "Speed Boost"

    def use(self, hero: Hero):
        if hero.health == hero.health:
            hero.health = hero.health
        else:
            hero.health += 50
        print(f"{hero.name} uses {self.name}. {self.effect} Now has {hero.health} HP.")


heroes = [Mage("Wizard", "Chain Lightning"), Warrior("Knight", "Dual Wield"), Archer("Elf", "Focus Fire")]
potions = [HealthPotion("Health Potion", "You regain 50 HP!"), ManaPotion("Mana Potion", "You restore 30 MP!"), SpeedBoost("Speed Boost", "Your speed increases for 10 seconds!")]

for hero in heroes:
    print(f"{hero.name} uses {hero.move}. {hero.name} has {hero.health} HP and {hero.speed} speed.")

for potion in potions:
    potion.use(heroes[0])