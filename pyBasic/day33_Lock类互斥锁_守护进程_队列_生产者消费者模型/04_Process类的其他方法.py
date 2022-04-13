import os
import time
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        super().__init__()

    def run(self):
        time.sleep(3)
        print(os.getppid(), os.getpid(), self.a, self.b, self.c)


if __name__ == '__main__':
        p = MyProcess(1, 2, 3)
        p.start()
        p.join()

        print(p.pid) # 26976
        print(p.ident) # 26976
        print(p.name) # MyProcess-1
        print(p.is_alive())
        time.sleep(1)
        p.terminate()   # 强制结束一个子进程  异步非阻塞（告诉操作系统要关闭子进程，什么时候关闭 并不关心）
        print(p.is_alive()) # 进程是否活着