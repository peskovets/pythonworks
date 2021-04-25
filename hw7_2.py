from abc import ABC, abstractmethod

class Сlothes(ABC):

    def __init__(self, name):
        self.name = name
        print(f"Создан предмет одежды под названием:{name}")

    @abstractmethod
    def abstract(self):
        print("Проверка на прочность")

    @property
    def tissue_consumption(self, size, height):
        consumption = self.size / 6.5 + 0.5 + self.height * 2 + 0.3
        print(consumption)
        return consumption


class Сoat(Сlothes):

    def __init__(self, name, size):
        super(Сoat, self).__init__(name)
        self.size = size
        print(f"Создано пальто {self.name} {size} размера")

    def abstract(self):
        print("Проверка на прочность")

    def tissue_consumption(self):
        consumption = int(self.size) / 6.5 + 0.5
        print(consumption)
        return consumption

class Suit(Сlothes):
    def __init__(self, name, height):
        super(Suit, self).__init__(name)
        self.height = height
        print(f"Создан костюм {self.name} на рост {self.height} ")

    def tissue_consumption(self):
        consumption = int(self.height) * 2 + 0.3
        print(consumption)
        return consumption

    def abstract(self):
        print("Проверка на прочность")

lab = Сoat('LAB', 52)
lab.tissue_consumption()
philipp_plein = Suit("Philipp Plein", 178)
philipp_plein.tissue_consumption()
