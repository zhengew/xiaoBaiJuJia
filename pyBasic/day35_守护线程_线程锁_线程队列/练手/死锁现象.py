# 死锁想象  同一个线程中存在多把互斥锁或递归锁
# from threading import Thread, Lock
#
# nood_lock = Lock()
# fork_lock = Lock()
#
# def eat1(name):
#     nood_lock.acquire()
#     print('%s抢到面条了'%name)
#     fork_lock.acquire()
#     print('%s抢到叉子了' % name)
#     print('%s吃完面了' % name)
#     nood_lock.release()
#     print('%s放下面条' % name)
#     fork_lock.acquire()
#     print('%s放下叉子' % name)
#
# def eat2(name):
#     fork_lock.acquire()
#     print('%s抢到叉子了' % name)
#     nood_lock.acquire()
#     print('%s抢到面条了' % name)
#     print('%s吃完面了' % name)
#     fork_lock.release()
#     print('%s放下面条' % name)
#     nood_lock.acquire()
#     print('%s放下叉子' % name)
#
# def main():
#     Thread(target=eat1, args=('alex',)).start()
#     Thread(target=eat2, args=('tbjx',)).start()
#     Thread(target=eat1, args=('wusir',)).start()
#     Thread(target=eat2, args=('ltt',)).start()
#
#     # alex抢到面条了tbjx抢到叉子了 同一个进程汇总有多个把互斥锁，导致死锁
#
# if __name__ == '__main__':
#     main()

# 解决死锁
from threading import Thread, RLock

noodle_fork_lock = RLock()

def eat1(name):
    noodle_fork_lock.acquire()
    print('%s抢到面条了'%name)
    print('%s抢到叉子了' % name)
    print('%s吃完面了' % name)
    noodle_fork_lock.release()
    print('%s放下面条' % name)
    print('%s放下叉子' % name)

def eat2(name):
    noodle_fork_lock.acquire()
    print('%s抢到叉子了' % name)
    print('%s抢到面条了' % name)
    print('%s吃完面了' % name)
    noodle_fork_lock.release()
    print('%s放下面条' % name)
    print('%s放下叉子' % name)

def main():
    Thread(target=eat1, args=('alex',)).start()
    Thread(target=eat2, args=('tbjx',)).start()
    Thread(target=eat1, args=('wusir',)).start()
    Thread(target=eat2, args=('ltt',)).start()
    # 死锁的根本原因就是在多个线程中使用多把互斥锁

if __name__ == '__main__':
    main()