# 守护线程，会一直守护到其他子线程都结束
import time
from threading import Thread

def func1():
    while True:
        print('in func1')
        time.sleep(1)

def func2():
    for i in range(3):
        print('in func2')
        time.sleep(0.5)

def main():
    t1 = Thread(target=func1)
    t1.daemon = True # 守护线程会随着主线程的结束而结束
    t1.start()

    t2 = Thread(target=func2)
    t2.start()


if __name__ == '__main__':
    main()