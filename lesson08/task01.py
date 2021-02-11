"""
Реализовать класс «Дата»,
функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать
число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date: str):
        tmp_date = list(Date.str_to_date(date))
        if not Date.check_date(*tmp_date):
            print('Ошибка в дате! Объект не создан')
            return
        self.day, self.month, self.year \
            = tmp_date

    @classmethod
    def str_to_date(cls, date):
        if len(date.split('-')) > 3:
            print('Неверный формат строки')
            return 0, 0, 0
        return map(lambda x: int(x), date.split('-'))

    @staticmethod
    def check_date(day, month, year):
        days_in_month = (0, 31, 28, 31, 30, 31, 30, 31,
                         31, 30, 31, 30, 31)
        if month not in range(1, 13):
            print(f'Ошибка! месяц {month} '
                  f'не в промежутке от 1 до 12')
            return False
        if day < 1 or day > days_in_month[month]:
            print(f'Ошибка! день {day} не в промежутке '
                  f'от 1 до количества дней '
                  f'{days_in_month[month]} в месяце {month}')
            return False
        _ = year
        return True


def main():
    date1 = Date('01-11-2000')
    print(date1.__dict__)

    date2 = Date('30-02-2000')
    print(date2.__dict__)

    date3 = Date('28-02-2000')
    print(date3.__dict__)

    date4 = Date('31-12-2000')
    print(date4.__dict__)

    date5 = Date('31-12-2000-000')
    print(date5.__dict__)


if __name__ == '__main__':
    main()
