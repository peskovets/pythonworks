class Worker:
    name = None
    surname = None
    position = None
    __income = {"wage": 0, "bonus": 0}

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        self.position = position
        self.name = name
        self.surname = surname
        self.__income = {"wage":wage, "bonus": bonus}

    def get_full_name(self):
        print(f"Сотрудник: {self.surname} {self.name}")

    def get_total_income(self):
        income = self.__income.get("wage") + self.__income.get("bonus")
        print(f"Доход {self.surname} составляет: {income}")

chef = Position("Ivan", "Ivanov", "director", 10000, 1000)
secretary = Position("Ivanova", "Mariya", "secretary", 5000, 500)

chef.get_full_name()
chef.get_total_income()

secretary.get_full_name()
secretary.get_total_income()

