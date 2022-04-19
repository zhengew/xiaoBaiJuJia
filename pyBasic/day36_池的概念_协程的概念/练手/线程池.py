# 线程池
import random
import time
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread

def func(a, b):
    print(current_thread().name, 'start', a, b)
    time.sleep(random.random())
    print(current_thread().name, 'end')


def main():
    tp = ThreadPoolExecutor(4) # 实例化线程池
    for i in range(12):
        tp.submit(func, i, i+1) # 异步提交任务

if __name__ == '__main__':
    main()