# 线程安全的单例模式
import time
from threading import Thread
# 线程安全的单例模式
class A:
    from threading import Lock
    __instance = None
    lock = Lock()
    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if not cls.__instance: # 如果是False，就开辟一块用于初始化的空间
                cls.__instance = super().__new__(cls)
        return cls.__instance

def func():
    a = A()
    print(a)

def main():
    for i in range(10):
        t = Thread(target=func)
        t.start()

if __name__ == '__main__':
    main()