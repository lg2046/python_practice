# class AlwaysEquals:
#     def __eq__(self, other):
#         return True
#
#     def __hash__(self):
#         return id(self)
#
#
# print(hash(AlwaysEquals()) == hash(AlwaysEquals))
#
# print(AlwaysEquals() == 1)
# print("google" == AlwaysEquals())
#
# print([hash(AlwaysEquals()) for i in range(5)])
#
# objects = [AlwaysEquals(), AlwaysEquals(), AlwaysEquals()]
# print([hash(obj) for obj in objects])


class SameHash:
    def __hash__(self):
        return 1


a = SameHash()
b = SameHash()

h = {a: '1', b: '2'}
print(h)
