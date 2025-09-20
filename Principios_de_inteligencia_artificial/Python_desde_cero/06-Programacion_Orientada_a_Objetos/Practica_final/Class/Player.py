import random


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.level = 1
        self.experience = 0

    def attack(self):
        return random.randint(10, 20) * self.level

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has muerto")
        else:
            print(f"Te quedan {self.health} de vida")

    def gain_experience(self, experience):
        print(f"Has ganado {experience} puntos de experiencia")
        self.experience += experience
        if self.experience >= 100:
            self.level += 1
            self.experience = 0
            print(f"{self.name} has subido a nivel {self.level}")
