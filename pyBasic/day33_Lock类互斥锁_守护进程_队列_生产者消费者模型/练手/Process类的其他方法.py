from multiprocessing import Process
import os

class MyProcess(Process):
    def __init__(self,name, age):
        super().__init__()
        self.name = name
        self.age = age

    def run(self):
        print('%s今年%s岁了'% (self.name, self.age))


def main():
    p = MyProcess('alex', 30)
    p.start()
    p.join()
    print(p.pid, p.name, p.ident)
    print(p.is_alive())
    p.terminate() # 强制结束子进程

if __name__ == '__main__':
    main()