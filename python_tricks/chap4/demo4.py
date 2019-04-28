from collections import namedtuple

User = namedtuple("User", ['name', 'obj', 'age'])

u = User('hello', object(), 42)
print(u.name)
print(u.obj)
print(u.age)

# 还保有序列特性
print(u[1])
print(*u, sep=':')

print(u._asdict())
print(tuple(u))
a, b, c = u  # 与tuple相同的性质
print(a, b, c, sep=":")


class SubUser(User):
    def hex_color(self):
        if self.age > 10:
            return "ka"
        else:
            return "ke"


u2 = SubUser('hello', object(), 42)
print(u2.hex_color())

ExtendUser = namedtuple('ExtendUser', User._fields + ('from',))

