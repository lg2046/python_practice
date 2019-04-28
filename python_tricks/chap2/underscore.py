class A:
    def __init__(self):
        self.name = "google"
        self.__name = "google"

    def get_name(self):
        return self.__name


if __name__ == '__main__':
    a = A()
    print(a.name)
    print(a.get_name())
