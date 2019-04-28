class Human:
    __count = 0
    a = 1

    def __init__(self, name, age):
        Human.__count += 1
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)

    @classmethod
    def get_human_count(cls):
        print(Human.__count)


class Student(Human):
    count = 0

    def __init__(self, name, age):
        super().__init__(name, age)
        self.__class__.count += 1

    def print_self(self):
        print(f'{self.__class__}: <name: {self.name}, age: {self.age}>')

    @classmethod
    def plus_sum(cls):
        return cls.count

    @staticmethod
    def helper():
        print("i am a helper")


class Parent(Human):

    def __init__(self, name, age):
        super().__init__(name, age)


def run():
    s = Student("andy", 10)
    s.print_self()
    [Student("andy", 10) for _ in range(10000)]
    [Parent("andy", 10) for _ in range(10000)]
    print(Student.count)
    print(Student.__dict__)
    print(s.__dict__)

    print(Student.plus_sum())
    Student.helper()
    s.get_name()

    Student.get_human_count()
    Human.get_human_count()

    print(Student.a)
    Student.a = 2
    print(Human.a)
    print(Student.a)
