from Class.Character import Character


class Hero(Character):
    #                 |  HERADADO  |
    def __init__(self, name, health, strength):
        # ATRIBUTOS HEREDADOS
        super().__init__(name, health)
        self.strength = strength

    def get_strength(self):
        print(f"{self.name} tiene el poder de {self.strength}")

