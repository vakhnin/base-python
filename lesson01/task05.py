"""
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""


def main():
    while True:
        income = int(input('Введите значение выручки (целое положительное число): '))
        if 0 <= income:
            break

    while True:
        expenses = int(input('Введите значение издержек (целое положительное число): '))
        if 0 <= expenses:
            break

    if expenses > income:
        print(f'Фирма работает с убутком. Убыток: {expenses - income}')
    else:
        print(f'Фирма работает с прибылью. Прибыль: {income - expenses}')
        print(f'Рентабельность: {(income - expenses) / income}')

        while True:
            count_staff = int(input('Введите численность '
                                    'сотрудников фирмы (целое положительное число): '))
            if 0 <= count_staff:
                break

        print(f'Прибыль на одного сорудника {(income - expenses) / count_staff}')


if __name__ == '__main__':
    main()