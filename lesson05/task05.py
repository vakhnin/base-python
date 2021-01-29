"""
Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
import os
from functools import reduce
from random import randint
COUNT_NUMBERS = 5


def main():
    try:
        with open(os.path.join('data', 'task05.txt'), 'w') as f:
            for _ in range(COUNT_NUMBERS):
                f.write(str(randint(1, 10)) + ' ')

        summa = 0
        with open(os.path.join('data', 'task05.txt')) as f:
            for content in f:
                summa += reduce(lambda x, y: x + y,
                                [int(n) for n in content.split()])
        print(f'Сумма чисел из файла: {summa}')
    except IOError:
        print('Произошла ошибка ввода-вывода!')


if __name__ == '__main__':
    main()
