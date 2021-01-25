"""
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(x, y, z):
    """Функция выдачи двух больших чисел из трех"""
    sorted_vals = sorted((x, y, z))
    return sorted_vals[-1] + sorted_vals[-2]


def main():
    x = int(input('Введите число x (целое число): '))
    y = int(input('Введите число y (целое число): '))
    z = int(input('Введите число z (целое число): '))

    print(my_func(x, y, z))


if __name__ == '__main__':
    main()
