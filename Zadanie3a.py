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
    """
    Klasa reprezentująca samochód. Zawiera informacje o marce, modelu i roku produkcji.
    """

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Inicjalizuje obiekt klasy Car.

        :param make: Marka samochodu (np. "Toyota").
        :param model: Model samochodu (np. "Corolla").
        :param year: Rok produkcji samochodu (np. 2022).
        """
        self.__make: str = make  # Prywatne pole przechowujące markę samochodu
        self.__model: str = model  # Prywatne pole przechowujące model samochodu
        self.__year: int = year  # Prywatne pole przechowujące rok produkcji samochodu

    @property
    def make(self) -> str:
        """
        Getter dla marki samochodu. Getter to metoda pozwalająca odczytać wartość pola.
        Dekorator @property oznacza, że metoda będzie wywoływana jakby była zwykłym polem.

        Przykład:
        car = Car("Toyota", "Corolla", 2022)
        print(car.make)  # Wywołanie tej metody zwróci wartość "__make".

        :return: Marka samochodu.
        """
        return self.__make

    @make.setter
    def make(self, make: str) -> None:
        """
        Setter dla marki samochodu. Setter to metoda pozwalająca ustawić nową wartość pola.
        Dekorator @make.setter oznacza, że można zmienić wartość pola "__make" przypisaniem.

        Przykład:
        car = Car("Toyota", "Corolla", 2022)
        car.make = "Honda"  # Wywołanie tej metody zmieni wartość "__make".

        :param make: Nowa marka samochodu.
        """
        self.__make = make

    @property
    def model(self) -> str:
        """
        Getter dla modelu samochodu.

        Przykład:
        car = Car("Toyota", "Corolla", 2022)
        print(car.model)  # Zwraca wartość "__model".

        :return: Model samochodu.
        """
        return self.__model

    @model.setter
    def model(self, model: str) -> None:
        """
        Setter dla modelu samochodu.

        Przykład:
        car = Car("Toyota", "Corolla", 2022)
        car.model = "Civic"  # Zmienia wartość "__model".

        :param model: Nowy model samochodu.
        """
        self.__model = model

    @property
    def year(self) -> int:
        """
        Getter dla roku produkcji samochodu.

        Przykład:
        car = Car("Toyota", "Corolla", 2022)
        print(car.year)  # Zwraca wartość "__year".

        :return: Rok produkcji samochodu.
        """
        return self.__year

    @year.setter
    def year(self, year: int) -> None:
        """
        Setter dla roku produkcji samochodu.

        Przykład:
        car = Car("Toyota", "Corolla", 2022)
        car.year = 2023  # Zmienia wartość "__year".

        :param year: Nowy rok produkcji samochodu.
        """
        if not isinstance(year, int):
            raise TypeError("Rok musi być typem integer!")

        if year <= 1886:
            raise ValueError("Samochody nie istniały przed 1886 rokiem!")

        self.__year = year

    def get_car_info(self) -> str:
        """
        Zwraca sformatowane informacje o samochodzie.

        Przykład:
        car = Car("Toyota", "Corolla", 2022)
        print(car.get_car_info())
        Wynik:
        Marka: Toyota
        Model: Corolla
        Rok produkcji: 2022

        :return: Łańcuch znaków zawierający markę, model i rok produkcji samochodu.
        """
        return (
            f"Marka: {self.__make}\n"
            f"Model: {self.__model}\n"
            f"Rok produkcji: {self.__year}"
        )

    def __str__(self) -> str:
        """
        Zwraca reprezentację tekstową obiektu Car.

        Przykład:
        car = Car("Toyota", "Corolla", 2022)
        print(car)
        Wynik:
        Marka: Toyota
        Model: Corolla
        Rok produkcji: 2022

        :return: Informacje o samochodzie w formacie tekstowym.
        """
        return self.get_car_info()


if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 2008)
    print(car1)
    print(car1.get_car_info())
    print(car1.make)
    print(car1.model)
    print(car1.year)
    car1.make = "Honda"
    print(car1.make)
    car1.model = "Civic"
    print(car1.model)
    car1.year = 2018
    print(car1.year)
    print(car1.get_car_info())

    # ta linijka zwróci coś takiego: <__main__.Car object at 0x106b07aa0>
    # żeby zwróciła faktyczne dane o samochodzie w taki sam sposób jak "get_car_info",
    # należy zaimplementować w klasie Car magiczną metodę __str__() - zrobiłem to ;)
    print(car1)
