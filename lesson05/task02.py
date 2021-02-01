"""
Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""
import os


def main():
    try:
        with open(os.path.join('data', 'task02.txt')) as f:
            strings_count = 0
            words_count = 0
            for content in f:
                strings_count += 1
                if content != '\n':
                    words_count += len(content.split())
    except IOError:
        print('Произошла ошибка ввода-вывода!')
    print(f'Количество строк:{strings_count} количество слов:{words_count}')


if __name__ == '__main__':
    main()
