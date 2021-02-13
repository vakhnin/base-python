"""
Создайте собственный класс-исключение,
обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):
    def __init__(self, text):
        self.txt = text


def main():
    while True:
        try:
            print('\nЕще раз')
            x = input('Введите делимое или "q", для выхода: ')
            if x == 'q':
                break
            x = int(x)
            y = input('Введите делитель или "q", для выхода: ')
            if y == 'q':
                break
            y = int(y)

            if y == 0:
                raise MyZeroDivisionError('Ошибка: на ноль делить нельзя!')
            print(f'{x}/{y}={x / y}')
        except ValueError:
            print('Ошибка: необходимо ввести число!')
            continue
        except MyZeroDivisionError as e:
            print(e.txt)


if __name__ == '__main__':
    main()
