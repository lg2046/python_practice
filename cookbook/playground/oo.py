# encoding: utf-8


class Student:
    level = "class_variable"  # 实例属性

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def print_score(self):
        print('%s %s %s' % (self.level, self._name, self._score))


lisa = Student('Lisa Simpson', 87)

print(Student.level)  # 打印类的level属性
print(lisa.level)  # level属性，因为实例并没有level属性，所以会继续查找class的level属性

lisa.level = "google"
print(lisa.level)
