"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда,
которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды
использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import abstractmethod, ABC


class Clothing(ABC):
    _name: str

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def tissue_consumption(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class Coat(Clothing):
    V: int

    def __init__(self, name, v):
        super().__init__(name)
        self.V = v

    def __str__(self):
        return f'Пальто "{self.name}" ' \
               f'требует ткани: {self.tissue_consumption}'

    @property
    def tissue_consumption(self):
        return self.V/6.5 + 0.5


class Suit(Clothing):
    H: int

    def __init__(self, name, h):
        super().__init__(name)
        self.H = h

    def __str__(self):
        return f'Костюм "{self.name}" ' \
               f'требует ткани: {self.tissue_consumption}'

    @property
    def tissue_consumption(self):
        return 2 * self.H + 0.3


class ClothesSet:
    def __init__(self):
        self.clothes_set = []

    def __str__(self):
        result = ''
        for item in self.clothes_set:
            result += str(item) + '\n'
        return result

    def __add__(self, other):
        self.clothes_set.append(other)

    @property
    def tissue_consumption(self):
        summa = 0
        for item in self.clothes_set:
            summa += item.tissue_consumption
        return summa


def main():
    clothes_set = ClothesSet()
    clothes_set + Suit('костюм 1', 1)
    coat2 = Coat('пальто 1', 1)
    coat2.name = 'пальто 2'
    clothes_set + coat2
    clothes_set + Suit('костюм 2', 1)

    print(clothes_set)
    print(f'Общий расход ткани: {clothes_set.tissue_consumption}')


if __name__ == '__main__':
    main()
