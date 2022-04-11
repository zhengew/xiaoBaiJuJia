from multiprocessing import Process
import os
def func():
    print(os.getpid(), os.getppid())

if __name__ == '__main__':
    print('main:', os.getpid(), os.getppid())
    p = Process(target=func)
    p.start()