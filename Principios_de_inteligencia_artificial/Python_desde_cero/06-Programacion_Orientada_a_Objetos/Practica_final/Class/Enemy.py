import random


class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self):
        return random.randint(5, 15)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"Has derrotado a {self.name}")
            return True
        return False
