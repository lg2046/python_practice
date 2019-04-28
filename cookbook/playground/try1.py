# import logging

try:
    print("try...")
    n = int('a')
    r = 10 / n
    print("result:", r)
except ValueError as e:
    print('ValueError', e)
    # logging.exception(e)  # 可以用来记录错误
except ZeroDivisionError as e:
    print("except:", e)
else:  # 没有异常会执行
    print("everything is ok")
finally:  # 总会执行
    print('finally...')

print('END')


# 异常的继承关系
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy


# 自定义异常并手动抛出
class FooError(ValueError):
    pass


# raise FooError('invalid value')

# try:
#     foo('0')
# except ValueError as e:
#     print('ValueError!')  记录异常后重新抛出原错误
#     raise
