class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, msg):
        print('   ' * self.level + msg)


if __name__ == '__main__':
    with Indenter() as indent:
        indent.print("HI")
        with indent:
            indent.print("gay")
            with indent:
                indent.print("gay")
            indent.print("haha")
        indent.print("reverse")
