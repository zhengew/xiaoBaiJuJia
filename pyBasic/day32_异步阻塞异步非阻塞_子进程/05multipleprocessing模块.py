# multiple 多元化的
# processing 进程
# multipleprocessing 多元的处理进程的模块

# from multiprocessing import Process
# import os
# def func():
#     print(os.getpid(), os.getppid())
#     # pid process id           进程id
#     # ppid parent process id   父进程id
#
# if __name__ == '__main__':
#     # 只会在主进程中执行的所有代码你写在 name = main 下
#     print('main:', os.getpid(), os.getppid())
#     p = Process(target=func)
#     p.start()

# main: 4921 725
# 4923 4921

# 为什么要用 if __name__ == '__main__':
# 能不能给子进程传递参数: 可以
# from multiprocessing import Process
# import os
# def func(name, age):
#     print(os.getpid(), os.getppid(),name, age)
#
# if __name__ == '__main__':
#     # 只会在主进程中执行的所有代码你写在 name = main 下
#     print('main:', os.getpid(), os.getppid())
#     p = Process(target=func, args=('alex',18))
#     p.start()
# main: 5893 725
# 5895 5893 alex 18


# 能不能获取子进程的返回值：# 不能，因为进程之间数据在内存中是隔离开的

# 能不能同时开启多个子进程：能
# from multiprocessing import Process
# import os
# import time
# def func(name, age):
#     print('%s start' % name)
#     time.sleep(1)
#     print(os.getpid(), os.getppid(),name, age)
#
# if __name__ == '__main__':
#     # 只会在主进程中执行的所有代码你写在 name = main 下
#     print('main:', os.getpid(), os.getppid())
#     arg_lst = [('alex',18), ('tbjx', 19), ('大壮', 28)]
#     for arg in arg_lst:
#         p = Process(target=func, args=arg)
#         p.start() # 异步非阻塞:
#         time.sleep(0.5) # mac太快了，不睡一下子进程执行的太快了...


## join的用法: # 阻塞：直到子进程执行完毕才继续执行代码
# import time
# from multiprocessing import Process
# import os
#
# def func(name, age):
#     print('发送一封邮件给%s岁的%s' %(age, name))
#     time.sleep(2)
#     print('发送完毕')
# if __name__ == '__main__':
#     arg_lst = [('alex', 18), ('tbjx', 19), ('大壮', 28)]
#     p_lst = []
#     for arg in arg_lst:
#         p = Process(target=func, args=('alex',18))
#         p.start()
#         p_lst.append(p)
#
#     for p in p_lst:
#         p.join() # 阻塞： 直到p这个子进程执行完毕才继续执行代码
#     print('所有的邮件已发送完毕')

# 同步阻塞和异步非阻塞
    # 同步阻塞
        # join
    # 异步非阻塞
        # start


# 多进程之间数据是否隔离: 是
from multiprocessing import Process
n = 0
def func():
    global n # 子进程中的全局变量，子进程与主进程之间是数据隔离的，
    n += 1

if __name__ == '__main__':
    p_l = []
    for i in range(100):
        p = Process(target=func)
        p.start()
        p_l.append(p)

    for p in p_l:
        p.join()
    print(n) # n = 0




# 使用多进程实现一个并发的socket的server端