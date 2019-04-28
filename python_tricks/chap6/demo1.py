my_items = ['a', 'b', 'c']

for i, ele in enumerate(my_items):
    print(i, ele, sep=":")

emails = {
    'Bob': 'bob@example.com',
    'Alice': 'alice@example.com',
}

for name, email in emails.items():
    print(f'{name} : {email}')

for i in range(0, 10, 2):
    print(i)

squares = [i * i for i in range(10)]  # for-loop的一种语法糖方式

# 等同于
# squares = []
# for i in range(10):
#     squares.append(i * i)
print(squares)

lst = [1, 2, 3, 4, 5]
print(lst[2:3:2])

print(lst[::2])
print(lst[::-1])
print(reversed(lst))

lst[:] = [7, 8, 9]
print(lst)  # [7, 8, 9]
lst[1:2] = [1, 2, 3]
print(lst)  # [7, 1, 2, 3, 9]
