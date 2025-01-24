# 11. Ćwiczenie dla kursantów
# Zadanie: System zwierząt
# Utwórz klasę bazową Animal z metodą make_sound().
# Dodaj klasy pochodne Dog, Cat i Cow, które implementują własne wersje make_sound().
# Napisz funkcję animal_sounds(animals), która iteruje po liście obiektów i wywołuje make_sound() dla każdego z nich.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Mooo!"



def animal_sounds(animals: list) -> None:
    for animal in animals:
        print(animal.make_sound())

def main():
    dog = Dog()
    cat = Cat()
    cow = Cow()
    animal_sounds([dog, cat, cow])

if __name__ == "__main__":
    main()





