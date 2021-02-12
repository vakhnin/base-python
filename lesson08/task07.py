"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} + {self.y}i'

    def __add__(self, other):
        if not isinstance(other, Complex):
            print('Второй параметр не комплексное число')
            return None
        return Complex(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if not isinstance(other, Complex):
            print('Второй параметр не комплексное число')
            return None
        return Complex(self.x * other.x - self.y * other.y,
                       self.y * other.x + self.x * other.y)


def main():
    print(Complex(3, 2) + Complex(1, 3))
    print(Complex(3, 2) * Complex(1, 3))


if __name__ == '__main__':
    main()
