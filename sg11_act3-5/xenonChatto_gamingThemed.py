class Hero():
    def __init__(self, name: str, health: int, move: str, speed: int, mana: int):
        self.name = name
        self.max_health = health
        self.health = health
        self.ability = move
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
        print(f"{self.name} shoots a precise arrow!")


class HealthPotion(Potions):
    def __init__(self, name: str, effect: str):
        super().__init__(name, effect)

    def use(self, hero: Hero):
        if hero.health == hero.max_health:
            print("Your health is already full!")
        else:
            hero.health = min(hero.health + 50, hero.max_health)

        print(f"{hero.name} uses {self.name}. {self.effect} Now has {hero.health} HP.")


class ManaPotion(Potions):
    def __init__(self, name: str, effect: str):
        super().__init__(name, effect)

    def use(self, hero: Hero):
        hero.mana += 30

        print(f"{hero.name} uses {self.name}. {self.effect} Now has {hero.mana} MP.")


class SpeedBoost(Potions):
    def __init__(self, name: str, effect: str):
        super().__init__(name, effect)

    def use(self, hero: Hero):
        hero.speed += 5

        print(f"{hero.name} uses {self.name}. {self.effect} Now has {hero.speed} speed.")

heroes = [
    Mage("Wizard", "Chain Lightning"),
    Warrior("Knight", "Dual Wield"),
    Archer("Elf", "Focus Fire")
]

potions = [
    HealthPotion("Health Potion", "You regain 50 HP!"),
    ManaPotion("Mana Potion", "You restore 30 MP!"),
    SpeedBoost("Speed Boost", "Your speed increases!")
]


def choose_character(character=None, potion=None, heroes=heroes, potions=potions):

    character = input("Choose your character (Wizard, Knight, Elf): ")
    selected_hero = None

    for hero in heroes:
        if character.lower() == hero.name.lower():
            selected_hero = hero
            print(f"You have chosen {hero.name}!")
            hero.move()
            break

    if selected_hero is None:
        print("Invalid character!")
        return

    potion = input("Choose your potion (Health, Mana, Speed): ")

    for potion_item in potions:
        if potion.lower() == potion_item.name.split()[0].lower():
            print(f"You have chosen {potion_item.name}!")
            potion_item.use(selected_hero)
            break
    else:
        print("Invalid potion!")


choose_character()