from Class.Character import Character


class Villian(Character):
    def __init__(self, name, health, ability):
        super().__init__(name, health)
        self.ability = ability

    def get_ability(self):
        print(f"{self.name} tiene la habilidad de {self.ability}")
