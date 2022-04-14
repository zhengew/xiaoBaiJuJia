# from threading import Thread, Lock
#
# n = 0
# def add(lock):
#     for i in range(220000):
#         global n
#         with lock:
#             n += 1
# def sub(lock):
#     for i in range(220000):
#         global n
#         with lock:
#             n -= 1
#
# t_l = []
# lock = Lock()
# for i in range(2):
#     t1 = Thread(target=add, args=(lock, ))
#     t1.start()
#     t2 = Thread(target=sub, args=(lock,))
#     t2.start()
#     t_l.append(t1)
#     t_l.append(t2)
#
# for t in t_l:
#     t.join()
#
# print(n)

'''
锁
0 LOAD_GLOBAL              0 (a)
2 LOAD_CONST               1 (1)
4 INPLACE_ADD
# GIL锁切换了
6 STORE_GLOBAL             0 (a)
释放锁
'''


# import time
# from threading import Thread, Lock
#
# n = []
# def append():
#     for i in range(5000000):
#         n.append(i)
# def pop(lock):
#     for i in range(5000000):
#         with lock:
#             if not n:
#                 time.sleep(0.00000001)
#             n.pop()
#
# t_l = []
# lock = Lock()
# for i in range(2):
#     t1 = Thread(target=append)
#     t1.start()
#     t2 = Thread(target=pop, args=(lock,))
#     t2.start()
#     t_l.append(t1)
#     t_l.append(t2)
#
# for t in t_l:
#     t.join()
#
# print(n)


# 不要操作全局变量，不要在类里操作静态变量
# += -+ *= /+ if while 数据不安全
# list dict 里的方法是线程安全的
# queue logging 模块是线程安全的

