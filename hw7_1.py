class Matrix:

    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for el in self.my_list:
            for i in el:
                print(f"{i:3}", end="")
            print()
        return ""

    def __add__(self, other):
        for el in range(len(self.my_list)):
            for el_2 in range(len(other.my_list[el])):
                self.my_list[el][el_2] = self.my_list[el][el_2] + other.my_list[el][el_2]
        return Matrix.__str__(self)



a = Matrix([[1, 2, 3], [2, 2 ,2]])
b = Matrix([[4, 5, 6], [7, 6, 6]])
print(a)
print(b)

c = a + b
print(c)