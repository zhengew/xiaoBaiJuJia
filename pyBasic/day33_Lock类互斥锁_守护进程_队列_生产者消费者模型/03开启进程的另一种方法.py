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
        print(os.getppid(), os.getpid(), self.a, self.b, self.c)


if __name__ == '__main__':
    print('-->', os.getpid())
    for i in range(10):
        p = MyProcess(1, 2, 3)
        p.start()