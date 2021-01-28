"""
Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from functools import reduce
from itertools import count


def fact():
    for i in count(1):
        yield reduce(lambda x, y: x * y, [j + 1 for j in range(i)], 1)


def main():
    generator = fact()
    i = 0
    for el in generator:
        if i > 10:
            break
        i += 1
        print(el)


if __name__ == '__main__':
    main()
