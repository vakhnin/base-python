"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user(name, surname, birth_year, city, email, phone):
    print(f'Имя:{name} Фамилия:{surname} Год рождения:{birth_year} '
          f'Город проживания:{city} email:{email} Телефон:{phone}')


def main():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    birth_year = input('Введите год рождения: ')
    city = input('Введите город проживания: ')
    email = input('Введите email: ')
    phone = input('Введите телефон: ')

    user(name=name, surname=surname, birth_year=birth_year,
         city=city, email=email, phone=phone)


if __name__ == '__main__':
    main()
