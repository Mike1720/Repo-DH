class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def identify(self):
        print(f"¡Hola! Soy {self.name}")

    def get_health(self):
        print(f"{self.name} tiene {self.health} puntos de salud")
