"""
Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета
и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import os
import re
from functools import reduce


def main():
    subjects_dict = {}
    try:
        with open(os.path.join('data', 'task06.txt'),
                  encoding='UTF-8') as f:
            for content in f:
                subjects, hours = content.split(':')
                # Как выделить учебные часы без регулярных выражений,
                # не придумал
                hours = re.findall(r'\d+', hours)
                hours = reduce(lambda x, y: x + y,
                                [int(n) for n in hours])
                subjects_dict[subjects] = hours

            print(subjects_dict)
    except IOError:
        print('Произошла ошибка ввода-вывода!')


if __name__ == '__main__':
    main()
