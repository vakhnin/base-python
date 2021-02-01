"""
Создать класс TrafficLight (светофор)
и определить у него один атрибут color (цвет)
и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться
только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from time import sleep


class TrafficLight:
    RED = 'красный'
    YELLOW = 'желтый'
    GREEN = 'зеленый'
    color_dict = {RED: {'duration': 7, 'next': YELLOW},
                  YELLOW: {'duration': 2, 'next': GREEN},
                  GREEN: {'duration': 4, 'next': RED}}

    __color = RED

    def running(self):
        for _ in range(20):
            print(f'Горит цвет: {self.__color}')
            sleep(self.color_dict[self.__color]['duration'])
            self.__color = self.color_dict[self.__color]['next']


def main():
    traffic_light = TrafficLight()
    traffic_light.running()


if __name__ == '__main__':
    main()
