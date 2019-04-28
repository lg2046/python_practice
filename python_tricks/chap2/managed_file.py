class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


from contextlib import contextmanager


@contextmanager
def managed_file(name):
    try:
        f = open(name, "w")
        yield f
    finally:
        f.close()


if __name__ == '__main__':
    file = ManagedFile("./test.log")
    with file as f:
        f.write("google")

    with managed_file("./ff.log") as f:
        f.write("haha")
