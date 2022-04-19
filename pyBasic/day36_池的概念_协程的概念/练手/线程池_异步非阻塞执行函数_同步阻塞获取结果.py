# 异步非阻塞执行任务，同步阻塞获取执行结果
import time
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread

def add(a, b):
    if a == 10: time.sleep(10) # 阻塞代码
    return current_thread().name, a+b

def main():
    tp = ThreadPoolExecutor(4)
    tp_dic = {} # 保存异步执行返回的future对象
    for i in range(20): # 异步非阻塞，执行add函数
        ret = tp.submit(add, i, i+1)
        tp_dic[i] = ret # 按照执行顺序将返回的future对象保存到tp_dic中
    # 同步阻塞，按照key的顺序获取future对象的结果看，
    # 如果结果没返回，就阻塞，等待结果返回
    # 例如：a == 10时，阻塞10秒，即使后面的线程已经执行完毕，也会先阻塞住，等待结果返回再继续执行
    for key in tp_dic:
        print(key)
        print(tp_dic[key].result())

if __name__ == '__main__':
    main()