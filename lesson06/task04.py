"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'У машины {self.name} скорость {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False

    def show_speed(self):
        print(f'У машины {self.name} скорость {self.speed}')
        if self.speed > 60:
            print(f'Машина {self.name} превышает скорость 60!!!')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False

    def show_speed(self):
        print(f'У машины {self.name} скорость {self.speed}')
        if self.speed > 40:
            print(f'Машина {self.name} превышает скорость 40!!!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


def main():
    town_car = TownCar(70, 'green', 'городской автомобиль')
    sport_car = SportCar(100, 'red', 'спортивный автомобиль')
    work_car = WorkCar(30, 'yellow', 'рабочий автомобиль')
    police_car = PoliceCar(150, 'white', 'полицейский автомобиль')

    print(f'Машина {town_car.name} - полицейская:{town_car.is_police}')
    print(f'Скорость {town_car.name}: {town_car.speed}')
    print(f'Цвет {town_car.color}: {town_car.color}')
    town_car.go()
    town_car.turn('на лево')
    town_car.turn('на право')
    town_car.show_speed()
    town_car.speed = 50
    town_car.show_speed()
    town_car.stop()
    print()

    print(f'Машина {town_car.name} - полицейская:{town_car.is_police}')
    print(f'Скорость {sport_car.name}: {sport_car.speed}')
    print(f'Цвет {sport_car.color}: {sport_car.color}')
    sport_car.go()
    sport_car.turn('на лево')
    sport_car.turn('на право')
    sport_car.show_speed()
    sport_car.stop()
    print()

    print(f'Машина {town_car.name} - полицейская:{town_car.is_police}')
    print(f'Скорость {work_car.name}: {work_car.speed}')
    print(f'Цвет {work_car.color}: {work_car.color}')
    work_car.go()
    work_car.turn('на лево')
    work_car.turn('на право')
    work_car.show_speed()
    work_car.speed = 50
    work_car.show_speed()
    work_car.stop()
    print()

    print(f'Машина {police_car.name} - полицейская:{police_car.is_police}')
    print(f'Скорость {police_car.name}: {police_car.speed}')
    print(f'Цвет {police_car.color}: {police_car.color}')
    police_car.go()
    police_car.turn('на лево')
    police_car.turn('на право')
    police_car.show_speed()
    police_car.speed = 50
    police_car.show_speed()
    police_car.stop()


if __name__ == '__main__':
    main()
