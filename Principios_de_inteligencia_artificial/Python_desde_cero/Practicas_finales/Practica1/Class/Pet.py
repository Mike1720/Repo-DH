class Pet:
    def __init__(self, name, age, health, price):
        self.name = name
        self.age = age
        self.health = health
        self.price = price

    def update_information(self, age=None, health=None, price=None):
        if age:
            self.age = age
        elif health:
            self.health = health
        elif price:
            self.price = price

    def get_info(self):
        return f"Mascota: {self.name}, Edad: {self.age}, Salud: {self.health}, Costo visita {self.price}"


class Dog(Pet):
    def __init__(self, name, age, health, price, breed, energy_level):
        super().__init__(name, age, health, price)
        self.breed = breed
        self.energy_level = energy_level

    def show_characteristics(self):
        return f"Raza: {self.breed}, Nivel de energia: {self.energy_level}"


class Cat(Pet):
    def __init__(self, name, age, health, price, breed, independence):
        super().__init__(name, age, health, price)
        self.breed = breed
        self.independence = independence

    def show_characteristics(self):
        return f"Raza: {self.breed}, Independencia: {self.independence}"
