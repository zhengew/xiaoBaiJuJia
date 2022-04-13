import time
from multiprocessing import Process

def func1():
    while True:
        print('in son1')
        time.sleep(1)

def func2():
    for i in range(10):
        print('in son2')
        time.sleep(1)

if __name__ == '__main__':
    p1 = Process(target=func1)
    p1.daemon = True  # 设置守护进程
    p1.start()

    p2 = Process(target=func2)
    p2.start()

    time.sleep(3)
    print('in main') # 守护进程在主进程代码执行完闭之后立即结束
    p2.join() # 主进程等待p2结束 - > 主进程的代码才结束 - > 守护进程结束