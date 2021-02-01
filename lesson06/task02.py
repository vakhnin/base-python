"""
Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина
* масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
* чи сло см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road():
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_weight(self, square_meter_weight, thickness):
        return self._length * self._width \
               * square_meter_weight * thickness


def main():
    road1 = Road(5000, 20)
    weight = road1.road_weight(25, 5)
    print(f'Масса дороги в тоннах:{weight/1000} '
          f'в килограммах:{weight}')


if __name__ == '__main__':
    main()
