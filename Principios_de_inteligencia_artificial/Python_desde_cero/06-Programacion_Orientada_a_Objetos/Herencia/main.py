from Class.Hero import Hero
from Class.Villian import Villian


superman = Hero("Superman", 100, "Volar")
joker = Villian("Joker", 100, "Robar")


superman.identify()  # Método heredado
superman.get_health()  # Método heredado
superman.get_strength()  # Método propio de la subclase


joker.identify()  # Método heredado
joker.get_health()  # Método heredado
joker.get_ability()  # Método propio de la subclase
