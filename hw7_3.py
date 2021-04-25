class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return Cell(self.quantity - other.quantity)
        else:
            print("Разность количества ячеек двух клеток меньше нуля")

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def make_order(self, instance):
        row = " "
        for i in range(int(self.quantity / instance)):
            row += f"{'*' * instance} \\n"
        row += f"{'*' * (self.quantity % instance)}"
        print(row)
        return row

a = Cell(50)
b = Cell(80)
c = a + b
print(c.quantity)
d = c - a
print(d.quantity)
d = c * a
print(d.quantity)
d = c / a
print(d.quantity)
c.make_order(3)
a.make_order(5)