"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle


def main():
    start = 3
    number_iter = count(start)
    print('Итератор count:')
    for i in number_iter:
        if i > 10:
            break
        print(i)

    iter_list = [7, 3, 6, 8]
    list_iter = cycle(iter_list)
    print('\nИтератор cycle:')
    i = 0
    for el in list_iter:
        if i > 10:
            break
        i += 1
        print(el)


if __name__ == '__main__':
    main()
