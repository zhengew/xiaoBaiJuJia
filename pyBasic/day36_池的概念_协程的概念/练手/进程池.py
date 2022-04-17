# 进程池
import os
import random
import time
from concurrent.futures import ProcessPoolExecutor

def func(a, b):
    print(os.getpid(), 'start', a, b)
    time.sleep(random.random())
    print(os.getpid(), 'end')

if __name__ == '__main__':
    tp = ProcessPoolExecutor(4) # 实例化进程池，池中有四个进程
    for i in range(20):
        tp.submit(func, a=i, b=i+1) # 异步提交任务