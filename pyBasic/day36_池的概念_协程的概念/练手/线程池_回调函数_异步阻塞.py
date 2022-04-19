# 线程池 回调函数，异步非阻塞执行函数，异步阻塞获取函数执行结果，哪个线程先执行完，就获取哪个线程的执行结果
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor

def add(a, b):
    return '%s:%s,%s'%(a, current_thread().name, a+b)

def print_result(ret): # 异步阻塞，打印ret对象绑定的回调函数获取的结果
    print(ret.result())

def main():
    tp = ThreadPoolExecutor(4)
    for i in range(20): # 异步非阻塞执行add函数
        ret = tp.submit(add, i, i+1)
        # 回调函数 异步阻塞，哪个future对象先返回结果，就立马执行print_result函数
        ret.add_done_callback(print_result)
if __name__ == '__main__':
    main()