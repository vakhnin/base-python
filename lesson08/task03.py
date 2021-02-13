"""
Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class MyValueException(Exception):
    def __init__(self, text):
        self.txt = text


def main():
    result_list = []
    while True:
        try:
            x = input('\nВведите число или "q", для выхода: ')
            if x == 'q':
                break
            if not x.isdigit():
                raise MyValueException('Ошибка: необходимо ввести число!')
            result_list.append(int(x))
            print(result_list)
        except MyValueException as e:
            print(e.txt)
            continue


if __name__ == '__main__':
    main()
