"""
Реализовать программу работы с органическими клетками.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр,
соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять
увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(),
принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает,
то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15,
количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, count: int):
        if count < 0:
            raise ValueError('Количество клеток '
                             'не может быть отрицательным')
        self.count = count

    def __add__(self, other):
        if not isinstance(other, Cell):
            raise NotImplemented('Операция не опреденена '
                                 'для не клеток')
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if not isinstance(other, Cell):
            raise NotImplemented('Операция не опреденена '
                                 'для не клеток')
        if self.count <= other.count:
            print('Вычитание невозможно! '
                  'Второй параметр не меньше первого.')
            return
        return Cell(self.count - other.count)

    def __mul__(self, other):
        if not isinstance(other, Cell):
            raise NotImplemented('Операция не опреденена '
                                 'для не клеток')
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        if not isinstance(other, Cell):
            raise NotImplemented('Операция не опреденена '
                                 'для не клеток')
        return Cell(round(self.count / other.count))

    def __str__(self):
        return str(f'Количество клеток: {self.count}')

    def make_order(self, row):
        result_str = ''
        count = self.count
        while count > row:
            result_str += '*' * row + '\n'
            count -= row
        result_str += '*' * count
        return result_str.strip()


def main():
    print('Сложение:')
    cell1 = Cell(1)
    print(cell1 + Cell(3) + Cell(2))
    # Так не получится:
    # Cell(1) + 1

    print('\nВычитание:')
    print(Cell(3) - Cell(2))
    print(Cell(3) - Cell(6))

    print('\nДеление:')
    print(Cell(3) / Cell(2))

    print('\nДеление:')
    print(Cell(3) / Cell(2))

    print('\nРасположение:')
    print(Cell(12).make_order(5))

    print('\nРасположение:')
    print(Cell(15).make_order(5))


if __name__ == '__main__':
    main()