"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""


def main():
    my_rating = [7, 5, 3, 3, 2]

    print('Текущий рейтинг:')
    print(my_rating)
    while True:
        number = input('Введите число (наберите "exit" для выхода): ')
        if number == 'exit':
            break
        number = int(number)

        not_found = True
        for i in range(len(my_rating)-1, -1, -1):
            if my_rating[i] > number:
                not_found = False
                my_rating.insert(i + 1, number)
                break
        if not_found:
            my_rating.insert(0, number)

        print('Текущий рейтинг:')
        print(my_rating)


if __name__ == '__main__':
    main()
