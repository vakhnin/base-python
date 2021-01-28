"""
Создать программно файл в текстовом формате,
записать в него построчно данные,
вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
import os


def main():
    try:
        with open(os.path.join('data', 'text.txt'), 'w') as f:
            while True:
                my_str = input('Введите строку для файла (Enter для выхода): ')
                if not my_str:
                    break
                f.write(my_str + '\n')
    except IOError:
        print('Произошла ошибка ввода-вывода!')


if __name__ == '__main__':
    main()
