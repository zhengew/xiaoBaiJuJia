import os
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        super().__init__()

    def run(self):
        print(os.getpid(), os.getppid(), self.a, self.b, self.c)


def main():
    print('main:', os.getpid(), os.getppid())
    for i in range(10):
        MyProcess(1, 2, 3).start()
if __name__ == '__main__':
    main()