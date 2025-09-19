from Class.Dog import Dog
from Class.Cat import Cat
from Class.Cow import Cow


def hacer_sonido_de_animal(animal):
    print(animal.hacer_sonido())


perro = Dog("Fenrir")
gato = Cat("Apolo")
vaca = Cow("Al")

hacer_sonido_de_animal(perro)
hacer_sonido_de_animal(gato)
hacer_sonido_de_animal(vaca)
