import time
from threading import Thread

def son():
    while True:
        print('in son')
        time.sleep(1)

def son2():
    for i in range(3):
        print('in son2 ***')
        time.sleep(1)

# flag a
t = Thread(target=son)
t.daemon = True
t.start()

Thread(target=son2).start()
# flag b

# 主线程会等待子线程结束之后才结束
# 为什么？
    # 主线程结束进程结束
# 守护线程随着主线程的结束而结束
# 守护线程会在主线程的代码结束之后继续守护其他子线程吗？会的


# 守护进程：会随着主进程的代码结束而结束，如果主进程代码结束之后还有其他子进程运行，守护进程不守护
# 守护线程：会随着主线程的结束而结束，如果主线程代码结束之后还有其他子线程在运行，守护线程也守护

# 为什么？
    # 守护进程和守护线程的结束原理不同
    # 守护进程需要主进程来回收资源
    # 守护线程是随着进程的结束才结束的
        # 其他子线程 - > 主线程结束 -> 主进程结束 -> 整个进程中所有的资源都被回收 - > 守护线程也会被回收

# 进程是资源分配单位
# 子进程都需要它的父进程来回收资源
# 线程是进程的资源
# 所有的线程都会随着进程的结束而被回收的