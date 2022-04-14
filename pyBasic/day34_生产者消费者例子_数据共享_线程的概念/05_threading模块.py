# import time
# import os
# from threading import Thread, current_thread, enumerate, activeCount
#
# def func(i):
#     print('start%s' % i,current_thread().ident)
#     time.sleep(1)
#     print('end%s' % i)
#
# if __name__ == '__main__':
#     tl = []
#     for i in range(10):
#         t =  Thread(target=func, args=(i,))
#         t.start()
#         print(t.ident, os.getpid())
#         tl.append(t)
#
#     print(enumerate(), activeCount())
#
#     for t in tl:t.join()
#
#     print('所有的线程都执行完了')

# current_thread() 获取当前所在的线程对象, current_thread().ident通过ident可以获取线程id
# 线程是不能从外部关闭的 terminate
# 所有的子线程只能是自己执行完代码之后就关闭
# enumerate 列表：存储了所有活着的线程对象,包括主线程
# activeCount 数字，存储所有或者的线程个数

# # 面向对象的方式起线程
# from threading import Thread
#
# class MyTherad(Thread):
#     def __init__(self, a, b):
#         super().__init__()
#         self.a = a
#         self.b = b
#
#     def run(self):
#         print(self.ident)
#
# t = MyTherad(1, 2)
# t.start() # 先开启线程，然后才在线程中执行run方法
# print(t.ident)

# 线程之间的数据的共享
from threading import Thread
n = 100

def func():
    global n
    n -= 1

t_l = []
for i in range(100):
    t = Thread(target=func)
    t.start()
    t_l.append(t)

for t in t_l:
    t.join()

print(n) # 0 验证线程之间的数据是共享的