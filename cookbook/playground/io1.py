with open("./io1.py", "r") as f:  # 以字符模式打开, 默认编码utf-8 file的__enter__()返回值作为f
    print(f.read(15), "|")  # 读15个字符  一个中文字算一个字符
    print(f.read(15), "|")  # 再读下15个字符 以免撑爆内存
    print(f.read(15), "|")
    print(f.read(15), "|")
    print(f.read())  # 一次性读完
#     结束with后调用#file的__exit__()


# 只要有read()方法，就称为file-like object， 比如文件   内存字节流 网络流

# read("...", "rb") # 以二进制模式打开，用于读图片 视频
with open("./io1.py", "rb") as f:
    print(f.read())
    # b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...'  # 十六进制表示的字节

# w wb用来写文本文件或二进制文件， 文件不存在会创建，会覆盖原文件, a追加模式
# 写文件时必须close()才会将没有写入的数据刷新到磁盘
with open("./test.log", "a") as f:
    f.write("hello baby2\n")

from io import StringIO

# 内存中的字符流
f = StringIO()

f.write("Hello")
f.write(" ")
f.write("world")

# getvalue获得写入后的str
print(f.getvalue())

# 用一个str初始化StringIO, 可以读
f = StringIO('hello\nhi\ngoodbay')
print(f.readline())  # 一行一行的读
print(f.readline())  # 如果是到末尾 返回空字符串
# BytesIO相当于StringIo的字节版


