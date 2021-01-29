"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу,
открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
import os


def main():
    translation_dict = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре',
    }

    try:
        with open(os.path.join('data', 'task04r.txt')) as f:
            output = ''
            for content in f:
                words = content.split()
                output += f'{translation_dict[words[0]]} - {words[2]}\n'
        output = output[:-1]

        with open(os.path.join('data', 'task04w.txt'),
                  'w', encoding='UTF-8') as f:
            f.writelines(output)
    except IOError:
        print('Произошла ошибка ввода-вывода!')


if __name__ == '__main__':
    main()
