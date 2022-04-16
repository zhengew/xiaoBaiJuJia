'''
# 有多少个任务就开多少个进程或线程
# 什么是池
    # 要在程序开始的时候，还没提交任务先创建几个线程或者进程
    # 放在一个池子里，这就是池

# 为什么要用池？
    # 如果先开好进程/线程，那么有任务之后就可以直接使用这个池中的数据
    # 并且开好的线程或者进程会一直存在池中，可以被多个任务反复利用
        # 这样极大的减少了开启/关闭/调度线程/进程的时间开销
    # 池中的线程/进程个数控制了操作系统需要调度的任务个数，控制池中的单位
        # 有利于提高操作系统的效率，减轻操作系统的负担

# 发展过程
# threading 模块 没有提供池
# multiprocessing 模块 仿照threading写的 Pool
# concurrent.futures 模块 线程池，进程池都能够用相似的方式开启/使用
'''
# 线程池
# import time
# import random
# from threading import current_thread
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
#
# def func(a, b):
#     print(current_thread().ident, 'start', a,b)
#     time.sleep(random.randint(1, 4))
#     print(current_thread().ident, 'end', )
#
# tp = ThreadPoolExecutor(4) # 实例化创建池
# for i in range(20):
#     tp.submit(func, i, b=i+1) # 异步提交任务

# 实例化 创建池
# 向池中提交任务，submit 传参数(按照位置传,按照关键字传)


# 进程池
# import time
# import random
# import os
# from threading import current_thread
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
#
# def func(a, b):
#     print(os.getpid(), 'start', a,b)
#     time.sleep(random.randint(1,4))
#     print(os.getpid(), 'end', )
#
# if __name__ == '__main__':
#     tp = ProcessPoolExecutor(4) # 实例化创建池
#     for i in range(20):
#         tp.submit(func, i, b=i+1) # 异步提交任务


##  获取任务结果

# import time
# import random
# import os
# from threading import current_thread
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
#
# def func(a, b):
#     print(os.getpid(), 'start', a,b)
#     time.sleep(random.randint(1,4))
#     print(os.getpid(), 'end', )
#     return a * b
#
# if __name__ == '__main__':
#     tp = ProcessPoolExecutor(4) # 实例化创建池
#     future_l = {}
#     for i in range(20): # 异步执行
#         ret = tp.submit(func, i, b=i+1) # 异步非阻塞
#         future_l[i] = ret
#         # print(ret.result()) # Future 未来对象
#     for key in future_l: # 同步阻塞(按照顺序获取)
#         print(key, future_l[key].result())


## map 只适合传递简单的参数，并且必须是一个可迭代的类型作为参数

# import time
# import random
# import os
# from threading import current_thread
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
#
# def func(a):
#     b = a + 1
#     print(os.getpid(), 'start', a,b)
#     time.sleep(random.randint(1,4))
#     print(os.getpid(), 'end', )
#     return a * b
#
# if __name__ == '__main__':
#     tp = ProcessPoolExecutor(4) # 实例化创建池
#     ret = tp.map(func, range(20))
#     # print(type(ret)) # <class 'generator'> 使用map方式，ret是个生成器
#     for key in ret: # 同步阻塞(按照顺序获取)
#         print(key)

## 回调函数：效率最高
import time
import random
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor

def func(a, b):
    print(current_thread().ident, 'start', a, b)
    time.sleep(random.randint(1,4))
    print(current_thread().ident, 'end', a)
    return (a, a * b) # 给一个标识符,记录返回结果的顺序

def print_func(ret): # 异步阻塞
    print(ret.result())

if __name__ == '__main__':
    tp = ThreadPoolExecutor(4) # 实例化创建池
    for i in range(20): # 异步执行 异步非阻塞
        ret = tp.submit(func, i, b=i+1) # 异步非阻塞
        ret.add_done_callback(print_func) # ret这个任务会在执行完毕的瞬间立即触发print_func函数，并且把任务的返回值对象传递到print_func作为参数
        # 异步阻塞 回调函数 给ret对象绑定一个回掉函数，等待ret对应的任务有了结果之后立即调用 print_func这个函数
        # 就可以对结果立即进行处理，而不用按照顺序接收结果处理结果

# 模拟回调函数
# import time
# import random
# import queue
# from threading import Thread
#
# def func(q,i):
#     print('start',i)
#     time.sleep(random.randint(1,5))
#     print('end',i)
#     q.put(i*(i+1))
#     # return i*i+1
# def print_func(q):
#     print(q.get())
#
# q = queue.Queue()
# for i in range(20):
#     Thread(target=func,args=(q,i)).start()
#
# for i in range(20):
#     Thread(target=print_func, args=(q,)).start()
