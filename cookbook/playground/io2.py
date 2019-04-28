# import os
#
# print(os.name)
# print(os.uname())  # 系统详细信息
#
# print(os.environ)  # 环境变量
# print(os.environ.get("JAVA_OPTS"), 'default')  # 环境变量
#
# # file and path
# print(os.path.abspath("."))  # 当前目录的绝对路径
# d = os.path.join("/Users/liguang/python_code/python/python_cookbook/playground", "testdir")
# print(d)
# os.makedirs(d)  # 可以递归创建目录
# # os.mkdir(d)
# os.rmdir(d)
#
# print(os.path.split(d))  # 返回元组后一部分是最后级别的目录或文件名
# print(os.path.dirname(os.path.dirname(d)))
#
# print(os.path.splitext("/google.txt"))  # 可以把文件与扩展名分开
#
# # os.rename('...', '...')
# # os.remove('test.py')
#
# # import shutil
# # shutil提供了很多函数作为os的补充
# # shutil.copyfile("a", "b")
#
#
# for f in os.listdir("."):
#     # 列出目录
#     if os.path.isdir(f):
#         print(f)
#     #     打印所有python文件
#     if os.path.isfile(f) and os.path.splitext(f)[1] == ".py":
#         print(f)


import pickle

d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))  # 序列化为bytes 然后就可以写入文件

with open("dump.txt", "wb") as f:
    pickle.dump(d, f)  # 直接存为文件

# pickle.loads(b"xxx") 从bytes中加载
with open("dump.txt", "rb") as f:
    print(pickle.load(f))  # 从文件中加载

# JSON
import json

print(json.dumps(d))  # dump写入文件
print(json.loads(json.dumps(d)))  # load从文件中加载


# 自定义序列对象
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    # 定义转换函数， 写在外面也行
    @staticmethod
    def student2dict(std):
        return {
            "name": std.name,
            "age": std.age,
            "score": std.score,
        }

    # 用于json.loads时转回对象
    @staticmethod
    def dict2student(d):
        return Student(d['name'], d['age'], d['score'])


s = Student('Bob', 20, 88)
j = json.dumps(s, default=Student.student2dict)
# {"name": "Bob", "age": 20, "score": 88}

print(json.loads(j, object_hook=Student.dict2student))

# 对于简单的可以直接使用__dict__, 可以dump出所有实例属性
s.attr1 = "value1"
print(json.dumps(s, default=lambda obj: obj.__dict__))
# {"name": "Bob", "age": 20, "score": 88, "attr1": "value1"}
