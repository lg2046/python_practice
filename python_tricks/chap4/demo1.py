a = [1, 2, 3]
b = a

print(a == b)  # True
print(a is b)  # True

a = [1, 2, 3]
b = list(a)

print(a == b)  # True
print(a is b)  # False


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'({self.name!r}, {self.age!r})')


s = Student("google", 10)

print(s)
print(f'{s}')
print(f'{s!r}')


class NameTooShortError(ValueError):
    pass


raise NameTooShortError("name")
