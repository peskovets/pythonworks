class Stationary:
    title: str
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationary):
    title = "ручка"
    def draw(self):
        print(f"{self.title} пишет")

class Pencil(Stationary):
    title = "карандаш"
    def draw(self):
        print(f"{self.title} черкает")

class Handle(Stationary):
    title = "маркер"
    def draw(self):
        print(f"{self.title} выделяет")

if __name__ == '__main__':
   stationary = Stationary()
   stationary.draw()

pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()

