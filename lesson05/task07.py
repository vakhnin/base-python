"""
Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл,
вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка:
[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json
import os


def main():
    try:
        analytic_dict = {}
        with open(os.path.join('data', 'task07.txt'),
                  encoding='UTF-8') as f:
            firm_count = 0
            profit_sum = 0
            for content in f:
                name, ownership, income, cost\
                    = content.split()
                profit = int(income) - int(cost)
                analytic_dict[name] = profit
                if profit >= 0:
                    firm_count += 1
                    profit_sum += profit

        average_profit = profit_sum / firm_count if firm_count else None
        result = [analytic_dict, {'average_profit': average_profit}]

        with open(os.path.join('data', 'task07.json'),
                  'w', encoding='UTF-8') as f:
            json.dump(result, f)
    except IOError:
        print('Произошла ошибка ввода-вывода!')


if __name__ == '__main__':
    main()
