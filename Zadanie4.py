# 11. Ćwiczenie dla kursantów
# Zadanie: System zwierząt
# Utwórz klasę Animal z atrybutem name i metodą make_sound.
# Dodaj klasy Dog i Cat, które dziedziczą z Animal.
# W klasach Dog i Cat nadpisz metodę make_sound

class Animal:
    def __init__(self, name: str):
        self.name: str = name

    def make_sound(self) -> str:
        return "Sound effect:"


class Dog(Animal):
    def make_sound(self) -> str:
        return f"{self.name} makes woof!"


class Cat(Animal):
    def make_sound(self) -> str:
        return f"{self.name} makes meow!"


if __name__ == "__main__":
    animal = Animal("Mammal")
    print(animal.make_sound())
    dog = Dog("Rex")
    print(dog.make_sound())
    cat = Cat("Gucio")
    print(cat.make_sound())
