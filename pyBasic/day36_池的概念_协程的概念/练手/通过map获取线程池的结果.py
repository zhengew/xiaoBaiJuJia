# map(func, *iterables) --> map object
# 这个跟map函数的用法几乎一样，只是通过线程池对象调用
import time
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread

def add(a):
    if a == 10:time.sleep(5)
    b = a+1
    return current_thread().name, a+b

def main():
    tp = ThreadPoolExecutor(4) # 实例化线程池对象
    ret = tp.map(add, range(20)) # 返回一个生成器对象,每次next获取一次执行结果
    for key in ret: # 同步阻塞，按顺序获取结果
        print(key)

if __name__ == '__main__':
    main()