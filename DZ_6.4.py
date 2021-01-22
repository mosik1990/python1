class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернул на право'

    def turn_left(self):
        return f'{self.name} повернул на лево'

    def show_speed(self):
        return f'{self.name}: текущая скорость {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} превышение скорости!'
        else:
            return f'{self.name} - дозволительная скорость'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'{self.name} превышение скорости!'
        else:
            return f'{self.name} - дозволительная скорость'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


Volvo = TownCar(90, 'Red', 'Volvo', False)
Nissan = SportCar(230, 'Black', 'Nissan', False)
Gazel = WorkCar(50, 'Gray', 'Gazel', False)
Vesta = PoliceCar(80, 'Blue', 'Vesta', True)
print(Volvo.show_speed())
print(Gazel.show_speed())
print(f'Марка: {Vesta.name}, цвет: {Vesta.color}')
print(f'{Vesta.name} - Полиция? {Vesta.is_police}')
print(f'{Nissan.name} - это Полиция? {Nissan.is_police}')
print(f'{Gazel.turn_left()}, а {Volvo.turn_right()}')