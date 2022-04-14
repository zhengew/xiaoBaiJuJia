# 单例模式
import multiprocessing
import time
class A():
    from threading import Lock
    __instance = None
    lock = Lock()
    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if not cls.__instance:
                time.sleep(0.00001) # cpu轮转 就会出问题
                cls.__instance = super().__new__(cls)
        return cls.__instance


def func():
    a = A()
    print(a)

from threading import Thread, Lock

for i in range(10):
    Thread(target=func).start()