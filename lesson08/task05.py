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


class Storage:
    storage: {}
    subdivisions = {}

    def __init__(self, subdivisions: tuple):
        self.storage = {}
        for el in subdivisions:
            self.subdivisions[el] = {}

    def __repr__(self):
        return str(self.storage) + '\n' + str(self.subdivisions)

    def add_position(self, equipment):
        self.storage[equipment] = 0

    def add_to_storage(self, item, count):
        self.storage[item] += count

    def move_to_subdivision(self, item, count, subdivision):
        if self.storage[item] - count < 0:
            print(f'Ошибка: Количество {self.storage[item]} '
                  f'"{item.name}" '
                  f'на складе меньше перемещаемого {count}')
            return
        self.storage[item] -= count
        if item in self.subdivisions[subdivision].keys():
            self.subdivisions[subdivision][item] += count
        else:
            self.subdivisions[subdivision][item] = count


def main():
    storage = Storage(('отдел1', 'отдел2'))

    xerox1 = Xerox('xerox1', 15000)
    storage.add_position(xerox1)

    scaner2 = Scaner('scaner2', 5000, is_hand_scaner=False)
    storage.add_position(scaner2)

    printer3 = Printer('printer3', 7000)
    storage.add_position(printer3)
    print(storage)

    print('\nДобавляем на склад:')
    storage.add_to_storage(xerox1, 3)
    storage.add_to_storage(scaner2, 1)
    print(storage)

    print('\nПереводим в отдел:')
    storage.move_to_subdivision(xerox1, 2, 'отдел1')
    print(storage)
    storage.move_to_subdivision(xerox1, 1, 'отдел1')
    print(storage)

    print('\nПытаемся перевести больше имеющегося на складе:')
    storage.move_to_subdivision(scaner2, 2, 'отдел2')


if __name__ == '__main__':
    main()
