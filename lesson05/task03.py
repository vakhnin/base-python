"""
Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
import os


def main():
    try:
        with open(os.path.join('data', 'task03.txt'),
                  encoding='UTF-8') as f:
            staff_count = 0
            salary_sum = 0
            for content in f:
                surname, salary = content.split()
                staff_count += 1
                salary_sum += int(salary)
                if int(salary) < 20000:
                    print(f'У сотрудника {surname} оклад меньше 20000:{salary}')
            if staff_count == 0:
                print('Список сотрудников пуст')
            else:
                print(f'Средняя зарплата:{salary_sum/staff_count}')
    except IOError:
        print('Произошла ошибка ввода-вывода!')


if __name__ == '__main__':
    main()
