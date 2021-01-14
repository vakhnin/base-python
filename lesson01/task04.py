"""
 Пользователь вводит целое положительное число.
 Найдите самую большую цифру в числе.
 Для решения используйте цикл while и арифметические операции.
"""


def main():
    while True:
        n = int(input('Введите целое положительное число: '))
        if n >= 0:
            break

    n_orig = n
    max_digit = n % 10
    n = n // 10

    while n > 0:
        if n % 10 > max_digit:
            max_digit = n % 10
        n = n // 10

    print(f'Максимальная цифра {max_digit} в числе {n_orig}')


if __name__ == '__main__':
    main()
