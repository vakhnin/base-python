"""
Реализовать скрипт, в котором должна быть предусмотрена
функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--hours', type=int)
    parser.add_argument('--rate', type=int)
    parser.add_argument('--bonus', type=int)
    args = parser.parse_args()
    print(f'ЗАрплата сотрудника: {args.hours * args.rate + args.bonus}')


if __name__ == '__main__':
    main()
