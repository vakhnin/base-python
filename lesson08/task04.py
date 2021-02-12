"""
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника»,
который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""


class Storage:
    storage: list

    def __init__(self):
        self.storage = []

    def __repr__(self):
        return str(self.storage)

    def add_to_storage(self, equipment):
        self.storage.append(equipment)


class Equipment:
    name: str
    price: int

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return '\n' + self.__class__.__name__ \
               + ': ' + str(self.__dict__)


class Printer(Equipment):
    is_jet_printer: bool

    def __init__(self, name, price, is_jet_printer=True):
        super().__init__(name, price)
        self.is_jet_printer = is_jet_printer


class Scaner(Equipment):
    is_hand_scaner: bool

    def __init__(self, name, price, is_hand_scaner=True):
        super().__init__(name, price)
        self.is_hand_scaner = is_hand_scaner


class Xerox(Equipment):
    is_two_sides: bool

    def __init__(self, name, price, is_two_sides=True):
        super().__init__(name, price)
        self.is_two_sides = is_two_sides


def main():
    storage = Storage()
    print(storage)
    print()

    storage.add_to_storage(Xerox('xerox1', 15000))
    print(storage)
    print()

    storage.add_to_storage(Scaner('scaner2', 5000, is_hand_scaner=False))
    print(storage)
    print()

    storage.add_to_storage(Printer('printer3', 7000))
    print(storage)
    print()


if __name__ == '__main__':
    main()
