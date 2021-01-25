"""
Реализовать формирование списка, используя функцию range()
и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def main():
    my_list = [i for i in range(100, 1001, 2)]
    multi_short = reduce(lambda x, y: x * y, my_list)
    print(multi_short)

    # Проверка правильности вычислений
    multi_long = 1
    for i in range(100, 1001, 2):
        multi_long *= i
    print(multi_long)
    print(multi_short == multi_long)


if __name__ == '__main__':
    main()
