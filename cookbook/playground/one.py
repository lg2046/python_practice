# 装饰器
# 装饰器就是一个返回函数的高阶函数
import functools


def log(func):
    def wrapper(*args, **kw):  # 新的函数把所有的参数都转到真正被调用的函数
        # 函数对角有一个__name__可以拿到函数的名字
        print('call %s():' % func.__name__)
        func(*args, **kw)

    return wrapper


@log  # 相当于执行了now = log(now)
def now():
    print("2018-03-01")


now()


# 如果需要接参数，就再写一个高阶函数
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):  # 新的函数把所有的参数都转到真正被调用的函数
            # 函数对角有一个__name__可以拿到函数的名字
            print('%s: call %s():' % (text, func.__name__))
            func(*args, **kw)

        return wrapper

    return decorator


@log2("google")  # 相当于执行了now = log2("google")(now)
def now2():
    print("2018-03-01")


now2()
print(now2.__name__)

int2 = functools.partial(int, base=2)

print(int2('1001'))
