"""
Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""


def main():
    x = 1
    y = 2

    print(x)
    print(y)

    x = int(input('Введите целое число: '))
    y = int(input('Введите целое число: '))
    s = input('Введите строку: ')

    print(f'Первое введенное число: {x}')
    print(f'Второе введенное число: {y}')
    print(f'Введенная строка: {s}')


if __name__ == '__main__':
    main()
