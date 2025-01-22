# 11. Ćwiczenie dla kursantów
# Zadanie: System zwierząt
# Utwórz klasę bazową Animal z metodą make_sound().
# Dodaj klasy pochodne Dog, Cat i Cow, które implementują własne wersje make_sound().
# Napisz funkcję animal_sounds(animals), która iteruje po liście obiektów i wywołuje make_sound() dla każdego z nich.

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow!"


class Cow(Animal):
    def make_sound(self) -> str:
        return "Mooo!"


def animal_sounds(animals: list) -> None:
    for animal in animals:
        print(animal.make_sound())


# Wywołanie kody powinno znaleźć się w funkcji main ;)
def main() -> None:
    dog = Dog()
    cat = Cat()
    cow = Cow()

    # Już funkcja `animal_sound` printuje informacje, więc poniżej print jedyne co robi, to
    # wyświetla na ekranie `None` jako ostatnią informację
    # lepiej więc pozbyć się tego printa:
    # print(animal_sounds([dog, cat, cow]))
    animal_sounds([dog, cat, cow])


# Dobrą praktyką jest używanie poniższego w skryptach ;)
if __name__ == '__main__':
    main()
