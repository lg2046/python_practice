import copy


#
# xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# ys = copy.copy(xs)
#
# xs[1][0] = 0
# print(ys)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'({self.name!r}, {self.age!r}, {self.grades!r}')


s = Student("google", 10)
s.grades.append(1)

s1 = copy.deepcopy(s)
s.name = "baidu"
s.grades.append(2)
print(s)
print(s1)
