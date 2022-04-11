# import os
# from multiprocessing import Process
#
# def func():
#     print(os.getpid(), os.getppid())
#
# if __name__ == '__main__':
#     print('main:', os.getpid(), os.getppid())
#     p = Process(target=func) # 实例化子进程
#     p.start() # 开启子进程
# main: 12849 725
# 12851 12849


# 给子进程传递参数
# from multiprocessing import Process
# import os
#
# def func(name, age):
#     print(os.getpid(), os.getppid(), name, age)
#
# if __name__ == '__main__':
#     print('main:', os.getpid(), os.getppid())
#     p = Process(target=func('alex', 18))
#     p.start()
# main: 13135 725
# 13135 725 alex 18


# join 同步阻塞： 直到子进程执行完毕才继续执行代码
# from multiprocessing import Process
# import time
# def func(name, age):
#     print('发送一封邮件给%s岁的%s' % (name, age))
#     time.sleep(1)
#     print('发送完毕')
#
# if __name__ == '__main__':
#     arg_lst = [('alex', 18), ('tbjx', 20), ('wusir', 22)]
#     p_lst = []
#     for arg in arg_lst:
#         p = Process(target=func, args=arg) # 参数args 接收元组，这个应该是个魔法参数
#         p.start()
#         p_lst.append(p)
#
#     for p in p_lst:
#         p.join() # 同步阻塞，直到p这个子进程执行完毕才继续执行
#
#     print('所有邮件发送完毕')
# 发送一封邮件给alex岁的18
# 发送一封邮件给tbjx岁的20
# 发送一封邮件给wusir岁的22
# 发送完毕
# 发送完毕
# 发送完毕
# 所有邮件发送完毕
# from multiprocessing import Process
# import time
# import os
# def func(name, age):
#     print('%s今年%s岁了'%(name, age))
#     time.sleep(1)
#     print('子进程pid%s,父进程ppid%s'%(os.getpid(), os.getppid()))
#
# if __name__ == '__main__':
#     arg_lst = [('alxe', 18), ('tbjx', 20), ('wusir', 25)]
#     p_lst = []
#     for arg in arg_lst:
#         # 参数args 接收元组，这个应该是个魔法形参 *args
#         p = Process(target=func, args=arg)
#         p.start()
#         p_lst.append(p)
#
#     for p in p_lst:
#         p.join() # 同步阻塞：阻塞子进程,直到p这个子进程执行完毕才继续执行代码
#     print('main',os.getpid(), os.getppid())
#     print('子进程全部执行完毕')

# alxe今年18岁了
# tbjx今年20岁了
# wusir今年25岁了
# 子进程pid14203,父进程ppid14201
# 子进程pid14204,父进程ppid14201
# 子进程pid14205,父进程ppid14201
# main 14201 725
# 子进程全部执行完毕