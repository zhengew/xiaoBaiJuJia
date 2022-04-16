# 守护进程随着主进程代码的结束而结束
import time
from multiprocessing import Process

def eat(name):
    print('%s 来吃饭了'%name)
def sleep(name):
    print('%s 来睡觉了'%name)
if __name__ == '__main__':
    usr_lst = ['alex', 'wusir', 'tbjx']
    for name in usr_lst:
        p1 = Process(target=eat, args=(name,))
        p1.daemon = True # 守护进程
        p1.start()
        p2 = Process(target=sleep, args=(name,))
        p2.start()
        time.sleep(1) # 如果不延迟，主进程代码瞬间结束，守护进程里的代码还没执行完就结束了，所以打印eat里的代码


# alex 来吃饭了
# alex 来睡觉了
# wusir 来吃饭了
# wusir 来睡觉了
# tbjx 来吃饭了
# tbjx 来睡觉了



