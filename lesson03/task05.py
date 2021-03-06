"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме
и после этого завершить программу.
"""


def sum_numbers_space_separated(string):
    """Функция сложения чисел в строке, разделенных пробелами"""
    return sum(map(lambda x: int(x), string.split()))


def main():
    summa = 0
    while True:
        inp = input('Введите числа, разделенные пробелами, символ q, для выхода: ')
        search_q_list = inp.split('q')
        summa += sum_numbers_space_separated(search_q_list[0])
        print(f'Текущая сумма: {summa}')
        if len(search_q_list) > 1:
            break


if __name__ == '__main__':
    main()
