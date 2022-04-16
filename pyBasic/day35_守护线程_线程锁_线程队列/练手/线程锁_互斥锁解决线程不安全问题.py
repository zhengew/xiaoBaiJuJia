# 互斥锁 解决线程不安全问题
# from threading import Thread, Lock
# num = 0
# def add(lock):
#     for i in range(200000):
#         global num
#         with lock:
#             num += 1
#
# def sub(lock):
#     for i in range(200000):
#         global num
#         with lock:
#             num -= 1
#
# if __name__ == '__main__':
#     lock = Lock()
#     t1 = Thread(target=add, args=(lock,))
#     t1.start()
#
#     t2 = Thread(target=sub, args=(lock,))
#     t2.start()
#
#     t1.join() # 必须是异步阻塞的
#     t2.join()
#
#     print(num) # 0


from threading import Thread, Lock

lst = []

def append():
    for i in range(200000):
        lst.append(i)

def pop(lock):
    for i in range(200000):
        with lock: # 互斥锁，确保在pop完赋值给list之后在开锁
            if lst:
                lst.pop()

if __name__ == '__main__':
    lock = Lock()
    t1 = Thread(target=append)
    t1.start()

    t2 = Thread(target=pop, args=(lock,))
    t2.start()

    t1.join()
    t2.join()
    print(lst)





