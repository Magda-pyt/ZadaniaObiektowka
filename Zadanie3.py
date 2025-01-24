# 9. Ćwiczenie dla kursantów
# Zadanie: Klasa Car
# Utwórz klasę Car z prywatnymi atrybutami:
# make (marka),
# model (model),
# year (rok produkcji).
# Dodaj metody:
# Getter i setter dla każdego atrybutu.
# Metodę get_car_info(), która zwróci informacje o samochodzie w postaci tekstu.


class Car:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.__make = make
        self.__model = model
        self.__year = year

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def get_car_info(self):
        return (f"Marka: {self.__make}\n"
                f"Model: {self.__model}\n"
                f"Rok produkcji: {self.__year}")

    def __str__(self) -> str:
        return self.get_car_info()


if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 2008)
    print(car1)
    print(car1.get_car_info())
    print(car1.get_make())
    print(car1.get_model())
    print(car1.get_year())
    car1.set_make("Honda")
    print(car1.get_make())
    car1.set_model("Civic")
    print(car1.get_model())
    car1.set_year(2018)
    print(car1.get_year())
    print(car1.get_car_info())

    # ta linijka zwróci coś takiego: <__main__.Car object at 0x106b07aa0>
    # żeby zwróciła faktyczne dane o samochodzie w taki sam sposób jak "get_car_info",
    # należy zaimplementować w klasie Car magiczną metodę __str__() - zrobiłem to ;)
    print(car1)
