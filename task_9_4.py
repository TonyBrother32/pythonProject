import random


class Car:

    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Поехали")

    def stop(self):
        print("Остановочка")

    def turn(self):
        i = random.randrange(1, 11)
        if i > 6:
            print("Поворот направо")
        else:
            print("Поворот налево")

    def show_speed(self):
        print(f"Ваша скорость {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, speed, colour, name, is_police):
        super().__init__(speed, colour, name, is_police)

    def show_speed(self):
        if int(self.speed) > 60:
            print(f'Вы превысили допустимую скорость в 60 км/ч, ваша скорость {self.speed}')
        else:
            print(f"Ваша скорость {self.speed} км/ч")


class SportCar(Car):
    def __init__(self, speed, colour, name, is_police):
        super().__init__(speed, colour, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, colour, name, is_police):
        super().__init__(speed, colour, name, is_police)

    def show_speed(self):
        if int(self.speed) > 40:
            print(f'Вы превысили допустимую скорость в 60 км/ч, ваша скорость {self.speed}')
        else:
            print(f"Ваша скорость {self.speed} км/ч")


class PoliceCar(Car):
    def __init__(self, speed, colour, name, is_police):
        super().__init__(speed, colour, name, is_police)


police = PoliceCar("80", "blue", "dodge", True)
police.show_speed()
print(f"Имя автомобиля {police.name}")
police.go()
police.turn()
police.stop()
print("-"*100)
tower_truck = WorkCar("50", "green", "ford", None)
tower_truck.show_speed()
print(f"Цвет автомобиля {tower_truck.colour}")
tower_truck.go()
tower_truck.turn()
tower_truck.stop()
print("-"*100)
cabriolet = SportCar("70", "red", "ferrari", None)
cabriolet.show_speed()
print(f"Это авто полиции ? {cabriolet.is_police}")
cabriolet.go()
cabriolet.turn()
cabriolet.stop()
print("-"*100)
taxi = TownCar("50", "yellow", "skoda", None)
taxi.show_speed()
print(f"Название авто {taxi.name}")
taxi.go()
taxi.turn()
taxi.stop()
