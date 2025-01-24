# 10. Ćwiczenie dla kursantów
# Zadanie 1:
# Utwórz klasę Student, która przechowuje:
#
# Imię i nazwisko studenta.
# Listę przedmiotów, które student studiuje. Dodaj metodę add_subject(subject), która dodaje przedmiot do listy.

class Student:
    def __init__(self, name: str, surname: str, subjects: list) -> None:
        self.name = name
        self.surname = surname
        self.subjects = subjects

    def present_yourself(self):
        return (f"Jestem studentem. Nazywam się: {self.name} {self.surname}. I uczę sie nastepujących przedmiotów:\n"
                f"{self.subjects}")

    def add_subject(self, new_subject: str) -> None:
        """
        Funkcja dodaje przedmioty nauczania do listy przedmiotów studenta i nie zwraca żadnej wartości.
        """
        self.subjects.append(new_subject)


if __name__ == "__main__":
    student1 = Student("Ala", "Nowak", ["matematyka", "fizyka", "chemia"])
    print(student1.present_yourself())
    student1.add_subject("biologia")
    print(student1.present_yourself())
