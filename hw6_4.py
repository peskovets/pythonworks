class Car:

    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = bool(is_police)
        print(f"Создан новый автомобиль марки {self.name}")

    def go(self):
        print(f"Автомобиль {self.name} поехал")

    def stop(self):
        print(f"Автомобиль {self.name} остановился")

    def turn(self, direction):
        print(f"Автомобиль повернул {direction}")

    def show_speed(self, speed):
        print(f"Скорость автомобиля {speed}")

class TownCar(Car):
    def __init__(self, name, speed, color, is_police, year):
        super(TownCar, self).__init__( name, speed, color, is_police)
        self.year = year
        print(f"Создан автомобиль марки {self.name} {self.year} года выпуска")

    def show_speed(self, speed):
        self.speed = speed
        if self.speed > 60:
            print(f"Скорость автомобиля превышена на {self.speed - 60} км")
        else:
            print(f"Скорость автомобиля составляет на {self.speed}  км/ч")

class SportCar(Car):
    pass

class WorkCar(Car):

    def __init__(self, name, speed, color, is_police, places):
        super(WorkCar, self).__init__( name, speed, color, is_police)
        self.places = places
        print(f"Создан автомобиль марки {self.name} на {self.places} мест")

    def show_speed(self, speed):
        self.speed = speed
        if self.speed > 40:
            print(f"Скорость автомобиля превышена на {self.speed - 40} км")
        else:
            print(f"Скорость автомобиля составляет на {self.speed}  км/ч")

class PoliceCar(Car):
    pass

opel = TownCar("Опель", 180, "черный", False, 1990)
ferarri = SportCar("Феррари", 300, "желтый", False)
ford = WorkCar("Форд", 120, "белый", False, 8)
police = PoliceCar("Бобик", 50, "синий", True)

opel.go()
opel.turn("налево")
opel.show_speed(100)
opel.stop

ferarri.go()
ferarri.turn("налево")
ferarri.show_speed(200)
ferarri.stop

ford.go()
ford.turn("налево")
ford.show_speed(200)
ford.stop

police.go()
police.turn("налево")
police.show_speed(10)
police.stop