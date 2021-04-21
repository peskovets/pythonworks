class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(f"Создана дорога длиной {self._length} метров и шириной {self._width} метров")

    def calculation(self, unit_weight, depth):
        result = self._width * self._length * unit_weight * depth / 100
        print(result)

trassa = Road(5000, 20)
trassa.calculation(25, 5)
