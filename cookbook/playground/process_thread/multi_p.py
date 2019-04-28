import os

# print("Process (%s) start..." % os.getpid())
#
# pid = os.fork()
#
# # 0代表子进程
# if pid == 0:
#     print("i am child process %s and parent is %s" % (os.getpid(), os.getppid()))
# else:
#     print("i am parent process %s" % (os.getpid()))


# multiprocess 抽象
# print("-----multiprocess-----")
# print("i am parent process %s" % (os.getpid()))
#
#
# def run_proc(name):
#     print("run child process %s is (%s)" % (name, os.getpid()))
#
#
# from multiprocessing import Process
#
# p = Process(target=run_proc, args=('test',))
#
# # 使用start启动进程
# p.start()
# # 等待进行完成
# p.join()
# print("child process end")

# # pool用于启动多个进程提交任务
# from multiprocessing import Pool
# import os, time, random
#
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
#
# print('Parent process %s.' % os.getpid())
# p = Pool(4)
# for i in range(5):
#     p.apply_async(long_time_task, args=(i,))
#
# print("提交完毕")
# # 禁止提交任务
# p.close()
# # 等待所有进程完成
# p.join()
# print("All subprocesses done")


# import subprocess
#
# # print('$ nslookup www.python.org')
# #
# # # 启动shell命令, 等待命令结束, 可以设一个超时 返回外部进程退出码
# # r = subprocess.call(['nslookup', 'www.python.org'])
#
# # print('Exit code:', r)
#
# # print(subprocess.run(['nslookup', 'www.python.org'], stdout=subprocess.PIPE))
# # CompletedProcess(args=['nslookup'...
#
#
# # 如果子进程还需要输入，则可以通过input输入：
# i = b'set q=mx\npython.org\nexit\n'
#
# print(subprocess.run(['nslookup'], input=i, stdout=subprocess.PIPE))
# import random
#
# from multiprocessing import Process, Queue
#
# import time
#
#
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
#
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
#
# # 建一个队列供于进程间通信 可以被传给启动进程的参数
# q = Queue()
#
# pw = Process(target=write, args=(q,))
# pw.start()
#
# pr = Process(target=read, args=(q,))
# pr.start()
#
# pw.join()
# pr.terminate()


# # python有GIL,只会在遇到IO操作才会释放GIL
# import time, threading
#
#
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 500:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
#
# print('thread %s is running...' % threading.current_thread().name)
#
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
#
# print('thread %s is running...' % threading.current_thread().name)
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

# import threading, multiprocessing
#
#
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1
#
#
# # 这里CPU的利用率只有100%，因为loop里面没有IO操作，所以任何时间只会占一个CPU
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()


import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
