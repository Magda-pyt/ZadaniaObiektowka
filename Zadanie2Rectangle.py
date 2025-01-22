# Zadanie 2:
# Utwórz klasę Rectangle, która przechowuje:
#
# Długość i szerokość. Dodaj metody area() (oblicza pole) i perimeter() (oblicza obwód).
from operator import length_hint


class Rectangle:
    def __init__(self, length: float, width: float):
        if length <= 0 or width <= 0:
            raise ValueError("Długosc i szerokosc prostokata muszą być większe od 0")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


if __name__ == "__main__":
    try:
        rectangle1 = Rectangle(2.0, 3.0)
        print(f"Pole prostokąta to {rectangle1.area()}")
        print(f"Obwód prostokąta to {rectangle1.perimeter()}")
    except ValueError as e:
        print(f"Błąd: {e}")
