from threading import Thread, RLock, Lock

def func(lock):
    lock.acquire() # 递归锁，支持锁多次
    lock.acquire()
    print('in func')
    lock.release()
    lock.release()

def main():
    lock = RLock()
    t1 = Thread(target=func, args=(lock,))
    t1.start()
    t2 = Thread(target=func, args=(lock,))
    t2.start()

if __name__ == '__main__':
    main()